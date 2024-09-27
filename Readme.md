# Mini LMS

Mini LMS is an online learning management system that allows teachers to create courses and quizzes, and students to enroll in courses and take quizzes. This project is built using Django.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Authentication (Login/Registration)
- Role-based Access (Student/Teacher)
- Course Management (Create, View, Edit, Delete)
- Quiz Management (Create, View, Edit, Delete)
- Quiz Submission and Result Viewing
- Responsive Design

## Project Structure
    db.sqlite3 
    envsmart/ 
        .gitignore 
        Lib/ 
        site-packages/ 
        pyvenv.cfg 
        Scripts/ 
            activate 
            activate_this.py 
            activate.bat 
            activate.fish 
            activate.nu 
            activate.ps1 
            deactivate.bat 
            django-admin.exe 
            normalizer.exe 
            pip-3.11.exe ... 
    lms/ 
        init.py 
        pycache/ 
        admin.py 
        apps.py 
        forms.py 
        migrations/ ... 
        models.py 
        static/ 
        templates/ 
        tests.py 
        utils.py 
        views.py 
        manage.py 
    mini_lms/ 
        init.py 
        pycache/ 
        asgi.py 
        settings.py 
        urls.py 
        wsgi.py 
    Readme.md 
    requirements.txt


### Key Directories and Files

- [`lms/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\"): Contains the main application code.
  - `models.py`: Defines the database models.
  - `views.py`: Contains the view functions.
  - `forms.py`: Defines the forms used in the application.
  - `templates/`: Contains the HTML templates.
  - `static/`: Contains static files like CSS and JavaScript.
- [`mini_lms/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Fmini_lms%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\mini_lms\"): Contains project settings and configurations.
  - `settings.py`: Django settings for the project.
  - `urls.py`: URL routing for the project.
- [`manage.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Fmanage.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\manage.py"): Django's command-line utility for administrative tasks.
- [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\requirements.txt"): Lists the Python dependencies for the project.

## Installation

### Prerequisites

- Python 3.11
- Django 3.x
- Virtualenv

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/mini_lms.git
   cd mini_lms

2. **Create a virtual environment:**
    ```sh
    python -m venv envsmart
    source envsmart/Scripts/activate  # On Windows
    # source envsmart/bin/activate    # On macOS/Linux

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt

4. **Apply migrations:**
    ```sh
        python manage.py migrate

5<vscode_annotation details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'>.</vscode_annotation> Create a superuser:
    python manage.py createsuperuser


