"""
ASGI config for telemed_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from core.routing import websocket_urlpatterns  # Ensure this exists

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telemed_project.settings')

# Application definition
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles HTTP requests
    "websocket": AuthMiddlewareStack(  # Handles WebSocket connections
        URLRouter(websocket_urlpatterns)
    ),
})



