#  Healthcare Backend API

A Django REST Framework backend for managing patients, doctors, and their mappings with JWT authentication.

---

##  Features

- JWT Authentication (Login & Refresh)
- Patient CRUD APIs
- Doctor CRUD APIs
- Assign doctors to patients
- Secure endpoints using Bearer Token

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (development)

---

##  Project Structure


healthcare_backend/
│
├── accounts/
├── config/
├── doctors/
├── patients/
├── mappings/
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md



---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/shuklaaanjaney/healthcare-backend.git
cd healthcare-backend

2️⃣ Create & activate virtual environment

python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Configure environment variables

Create a .env file in the project root and added:
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

.env is ignored by Git for security reasons.

5️⃣ Run database migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create admin user 
python manage.py createsuperuser

7️⃣ Run the development server
python manage.py runserver

Server will start at:
http://127.0.0.1:8000/

>>> Authentication (JWT)
Login

POST /api/auth/login/
{
  "username": "your_username",
  "password": "your_password"
}

Response:
{
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}

Use the access token as:

Authorization: Bearer <access_token>

>>> API Endpoints
Patients
 1: GET /api/patients/
 2: POST /api/patients/
 3: PUT /api/patients/{id}/
 4:DELETE /api/patients/{id}/

Doctors
 1: GET /api/doctors/
 2: POST /api/doctors/
 3: PUT /api/doctors/{id}/
 4: DELETE /api/doctors/{id}/

Assign Doctor to Patient

 POST /api/mappings/assign/
 {
  "patient": 1,
  "doctor": 1
}

🧪 Testing

All APIs were tested using Postman with JWT Bearer authentication.