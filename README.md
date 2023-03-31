# MowebTask
Practical Task

Steps to setup the project : 
1) git clone git@github.com:kb9101/MowebTask.git
2) Create a virtual environment : python -m venv venv
3) Activate the virtual environment : source venv/bin/activate (for linux) and venv/Scripts/activate (for windows)
4) Install the requirements.txt file : pip install -r requirements.txt
5) Change the database credentials in settings.py file
6) Make migrations : python manage.py migrate
7) Create super user : python manage.py createsuperuser
7) Run the project : python manage.py runserver
8) By default DRF browsable API would open on : http://127.0.0.1:8000
9) Open the swagger ui : http://127.0.0.1:8000/swagger
10) On the swagger ui page generate token from api-auth-token by providing your super user credentials
11) Create a company first otherwise it will give error in creating an employee.
12) When an employee is created, an email would be sent to the email address provided at the time of creating an employee.
13) The process of sending email when employee gets registered is done through the use of signals.
14) You can check if the cron job is running or not with the command : python manage.py runcrons
15) When you run cron job, it would send a happy birthday email to sanjay@moweb.com.
15) By following these steps you can easily navigate through the project.
