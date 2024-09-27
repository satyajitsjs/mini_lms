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
- Django 5.1.1
- Virtualenv

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/mini_lms.git
   cd mini_lms
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv envsmart
   source envsmart/Scripts/activate  # On Windows
   # source envsmart/bin/activate    # On macOS/Linux
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

7. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

### User Roles

- **Student**: Can view and enroll in courses, take quizzes, and view their results.
- **Teacher**: Can create, view, edit, and delete courses and quizzes, and view all quiz submissions.

### Key URLs

- **Home Page**: [`/`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Findex.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A61%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fstudent%2Fview_marks.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A19%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fstudent%2Fstudentclick.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A39%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fcourse_view.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A26%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fcreate_course.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A10%2C%22character%22%3A1%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fteacher_quiz.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A26%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fview_all_course.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A18%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fteacherclick.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A6%2C%22character%22%3A41%7D%7D%5D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "Go to definition")
- **Student Dashboard**: `/student/dashboard/`
- **Teacher Dashboard**: `/teacher/dashboard/`
- **Login**: `/login/`
- **Register**: `/register/`

### Templates

- **Base Template**: [`lms/templates/base.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fbase.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\base.html")
- **Dashboard Base Template**: [`lms/templates/dashboard_base.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fdashboard_base.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\dashboard_base.html")
- **Student Templates**: [`lms/templates/student/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fstudent%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\student\")
  - [`view_marks.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fstudent%2Fview_marks.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\student\view_marks.html")
  - [`studentclick.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fstudent%2Fstudentclick.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\student\studentclick.html")
- **Teacher Templates**: [`lms/templates/teacher/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\teacher\")
  - [`create_course.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fcreate_course.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\teacher\create_course.html")
  - [`view_all_quiz.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fview_all_quiz.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\teacher\view_all_quiz.html")
  - [`teacherclick.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fteacherclick.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\teacher\teacherclick.html")
  - [`view_all_submission.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fview_all_submission.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\teacher\view_all_submission.html")
  - [`view_all_course.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fview_all_course.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\teacher\view_all_course.html")
  - [`course_view.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2Fmini_lms%2Flms%2Ftemplates%2Fteacher%2Fcourse_view.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227ef96970-c8bb-4986-a229-aafcbda8cc9a%22%5D "c:\Users\satya\OneDrive\Desktop\mini_lms\lms\templates\teacher\course_view.html")

### Example Code

#### View All Submissions (Teacher)

```python
@login_required(login_url='/login')
def view_all_submission(request):
    submissions = StudentQuizSubmission.objects.filter(quiz__course__teacher=request.user)
    return render(request, 'teacher/view_all_submission.html', {'submissions': submissions})
```

#### View Results (Student)

```python
@login_required
def view_results(request):
    courses = Course.objects.filter(enrollment__student=request.user)
    submissions = StudentQuizSubmission.objects.filter(student=request.user)
    context = {
        'courses': courses,
        'submissions': submissions
    }
    return render(request, 'student/view_results.html', context)
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This README.md provides a comprehensive overview of your project, including its features, structure, installation steps, usage, and contribution guidelines. Adjust the content as needed to fit your specific project details.
