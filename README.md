# 🩺 HEALTH CARE BACKEND

This is the backend service for the Health Care application. It is built using Django and provides APIs for managing authentication, doctors, patients, and mappings.

## 🧰 Features

- User authentication and authorization
- Doctor management
- Patient management
- Data mappings and relationships

## 🏵️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Ashoksanaka/Healthcare-Backend.git
cd healthcare_backend
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Generate migrations:

```bash
python manage.py makemigrations
```

2. Apply migrations:

```bash
python manage.py migrate
```

3. Run the development server:

```bash
python manage.py runserver
```

4. The API will be available at `http://127.0.0.1:8000/`

## 📝 Project Structure

- `authentication/` - Handles user authentication and authorization
- `doctors/` - Manages doctor-related data and APIs
- `patients/` - Manages patient-related data and APIs
- `mappings/` - Handles data mappings and relationships between entities
- `healthcare/` - Project settings and configuration


⚠️ Note: The API endpoints have been successfully tested using Postman API tool.
