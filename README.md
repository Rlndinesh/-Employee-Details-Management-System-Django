# Employee Details Management System (Django)

This is a Django-based web application for managing and displaying employee details.  
The project includes an `employees` app, HTML templates, media handling, and uses SQLite as the default database.

---

## Project Structure
```text
mysite/
│
├── employees/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/
│
├── mysite/
│   ├── static/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── templates/
│   ├── home.html
│   └── employee_detail.html
│
├── db.sqlite3
└── manage.py

```
---

## Features

- Display employee details
- Django Admin panel integration
- Template-based frontend
- Media file support
- SQLite database (default)

---

## Tech Stack

- Backend: Python, Django
- Frontend: HTML, CSS
- Database: SQLite
- Framework: Django MVT Architecture

---

## Prerequisites

Make sure the following are installed:

- Python 3.8 or higher
- pip
- Virtualenv (recommended)

---

## Setup Instructions

### 1. Clone the Project
```
git clone https://github.com/your-username/employee-details.git  
cd mysite
```
---

### 2. Create and Activate Virtual Environment

Windows:
```
python -m venv env  

```
```
env\Scripts\activate  
```
Mac/Linux:
```
python3 -m venv env  
```
```
source env/bin/activate  
```
---

### 3. Install Dependencies

```
pip install django  
```
(Optional)
```
pip install -r requirements.txt
```
---

### 4. Apply Migrations
```
python manage.py makemigrations  
```
```
python manage.py migrate  
```
---

### 5. Create Superuser (Optional)
```
python manage.py createsuperuser  
```
Used to access Django Admin.

---

### 6. Run the Development Server
```
python manage.py runserver  
```
---

## Access URLs

- Home Page: http://127.0.0.1:8000/
- Employee Detail Page: http://127.0.0.1:8000/employees/
- Admin Panel: http://127.0.0.1:8000/admin/

---

## Templates

- home.html → Landing page
- employee_detail.html → Displays employee information

---

## Media & Static Files

- Media files are stored in the `media/` directory
- Static files are managed inside `mysite/static/`

---

## Database

- SQLite database file: `db.sqlite3`
- Models are defined in `employees/models.py`

---

## Future Enhancements

- Employee CRUD operations
- Authentication & authorization
- Search and filter employees
- REST API integration
- Deployment to cloud platforms

---

## Author

https://github.com/Rlndinesh

https://rlndinesh.github.io/portfolio/