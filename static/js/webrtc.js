const localVideo = document.getElementById("localVideo");
const remoteVideo = document.getElementById("remoteVideo");
let peerConnection;
let localStream;

const config = {
  iceServers: [{ urls: "stun:stun.l.google.com:19302" }],
};

const socket = new WebSocket("ws://" + window.location.host + "/ws/video/");

navigator.mediaDevices
  .getUserMedia({ video: true, audio: true })
  .then((stream) => {
    localVideo.srcObject = stream;
    localStream = stream;
  })
  .catch((error) => {
    console.error("Error accessing media devices.", error);
  });

socket.onmessage = async (event) => {
  const data = JSON.parse(event.data);

  if (data.type === "offer") {
    await peerConnection.setRemoteDescription(new RTCSessionDescription(data));
    const answer = await peerConnection.createAnswer();
    await peerConnection.setLocalDescription(answer);
    socket.send(JSON.stringify(peerConnection.localDescription));
  } else if (data.type === "answer") {
    await peerConnection.setRemoteDescription(new RTCSessionDescription(data));
  } else if (data.type === "candidate") {
    await peerConnection.addIceCandidate(new RTCIceCandidate(data.candidate));
  }
};

function startCall() {
  peerConnection = new RTCPeerConnection(config);

  localStream.getTracks().forEach((track) => {
    peerConnection.addTrack(track, localStream);
  });

  peerConnection.ontrack = (event) => {
    remoteVideo.srcObject = event.streams[0];
  };

  peerConnection.onicecandidate = (event) => {
    if (event.candidate) {
      socket.send(
        JSON.stringify({ type: "candidate", candidate: event.candidate })
      );
    }
  };

  peerConnection
    .createOffer()
    .then((offer) => peerConnection.setLocalDescription(offer))
    .then(() => {
      socket.send(JSON.stringify(peerConnection.localDescription));
    });
}

socket.onopen = () => {
  startCall();
};
