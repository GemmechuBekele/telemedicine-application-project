# 🏥 Telemedicine Application

This is a Django-based **Telemedicine Web Application** that allows **patients** to book appointments with **doctors**, manage their profiles, and initiate video calls. Doctors can manage their appointments and communicate with patients through the platform.

---

## 🚀 Features

- Patient and Doctor role-based sign-up and login
- Book appointments with specific doctors
- View dashboard with upcoming appointments
- Real-time video calls using WebRTC
- Authentication using Django's built-in auth system
- REST API endpoint for booking via `POST` requests

---

## 📁 Project Structure

telemedicine-application-project/

├── core/ # Main app containing views, models, forms

├── telemed_project/ # Django project settings

├── templates/ # HTML Templates

├── static/ # JavaScript, CSS files

├── db.mysql # MYSQL database 

├── manage.py # Django project manager

└── README.md # This file


---

## 🧰 Technologies Used

- Python 3.10+
- Django 4.x
-  MySQL
- WebRTC (for real-time video calls)
- Channels (optional for signaling with WebSockets)
- HTML, CSS, JS (frontend)

---

## 🔧 Installation & Setup

### Step 1: Clone the Repository

```bash 
git clone https://github.com/your-username/telemedicine-application-project.git
cd telemedicine-application-project

### step 2 :  Create & Activate Virtual Environment
#### On macOS/Linux:
python3 -m venv env
source env/bin/activate
#### On Windows:
python -m venv env
env\Scripts\activate

### Step 3: Install Dependencies
pip install -r requirements.txt

- If requirements.txt is missing, install manually:
pip install django

### Step 4: Apply Migrations
python manage.py makemigrations
python manage.py migrate

### Step 5: Create Superuser
python manage.py createsuperuser

 `Visit: http://127.0.0.1:8000/`

 ## 👥 User Roles
 - Patients can sign up, view doctors, and book appointments.
- Doctors can sign up, manage their availability, and conduct video calls.
- Admins can manage all models via Django Admin panel at /admin/.

## 👨‍💻 Contributing
`- Pull requests are welcome! For major changes, open an issue first to discuss what you would like to change.`

## 🔗 Connect
`- Feel free to follow or fork the project. Have feedback or need help? Open an issue!`
