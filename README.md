
# Task API

This repository contains the code for a RESTful API implemented in Django, focusing on task management with user authentication using JWT. It includes CRUD operations for tasks and user registration.

## Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Virtualenv](https://pypi.org/project/virtualenv/)
- [Git](https://git-scm.com/downloads/)
- [Django](https://www.djangoproject.com/)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/lokeshdarla/todo-list-Django.git
cd todo-list-Django
```

### 2. Set up Virtual Environment

```bash
# On Unix or MacOS
python3 -m venv venv

# On Windows
python -m venv venv
```

### 3. Activate Virtual Environment

```bash
# On Unix or MacOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Run the test cases

```bash
python3 manage.py test 
```
