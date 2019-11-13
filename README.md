# SalaryManagement

Local development steps :
1. Clone repository locally
2. Create your virtual environment
3. python3 -m venv /path/to/new/virtual/environment
4. Start virtual environment
5. source /path/to/new/virtual/environment/bin/activate
6. Configure your virtual environment with file included in repo
7. Initialize db.sqlite3 database
8. python manage.py migrate
9. python manage.py makemigrations

Project Dependencies:
1. certifi==2019.3.9
2 .chardet==3.0.4
3. Django==2.1.7
4. djangorestframework==3.9.1
5. idna==2.8
6. pycodestyle==2.5.0
7. pytz==2018.9
8. requests==2.21.0
9. urllib3==1.24.1

ADMIN :
1. create SuperUser
2. python manage.py createsuperuser
3. Start server
4. python manage.py runserver

Admin login:
http://127.0.0.1:8000/admin/

operations :
1. Do CRUD operations on employee.
2. Do CRUD operations on salary of the employee(Payslips).


Employee login:
http://127.0.0.1:8000/login

Home page - http://127.0.0.1:8000/home
- The Home page navigates to other page
1. view employee profile.
2. view salary details.
3. Logout
4. change password
5. About






