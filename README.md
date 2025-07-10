# HEALTH CARE BACKEND

This is the backend service for the Health Care application. It is built using Django and provides APIs for managing authentication, doctors, patients, and mappings.

## Features

- User authentication and authorization
- Doctor management
- Patient management
- Data mappings and relationships

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd healthcare_backend
```

2. Create and activate a virtual environment:

```bash
python3 -m venv health_venv
source health_venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Apply migrations:

```bash
python manage.py migrate
```

2. Run the development server:

```bash
python manage.py runserver
```

3. The API will be available at `http://127.0.0.1:8000/`

## Project Structure

- `authentication/` - Handles user authentication and authorization
- `doctors/` - Manages doctor-related data and APIs
- `patients/` - Manages patient-related data and APIs
- `mappings/` - Handles data mappings and relationships between entities
- `healthcare/` - Project settings and configuration

## Running Tests

To run the tests for all apps, use:

```bash
python manage.py test
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.
