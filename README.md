To run locally, do the usual:

#. Create a Python 3.6 virtualenv

    Django 1.11 version installed
   
#. Create project projectname

    django-admin startproject studentfeedbackproject
   
#. Go to the project dir
    cd studentfeedbackproject
    
#. Create application inside main project directory

     py manage.py startapp testapp
   
#. Configure the templatefile and staticfile inside settings.py
   create template folder and static folder, inside static folder create css file
   Here sqlite used as default database
   
#. Create model class student with attributes
   
#.To convert model class to sql code use makemigrations

    py manage.py makemigrations
   
#. To create table inside database

    py manage.py migrate
   
#. Create superuser to connect with database

    py manage.py createsuperuser
   
#. Create a django form inside testapp

#. For form validation process two methods are used Implicit validation by django and Explicit validation by user
   Clean method is used for explicit validation
   Explicit validations are
   
    Name field should contain atleast 4 characters otherwise it will show validation error
   
    Roll No field should contain atleast 3 characters otherwise it will show validation error
   
    Email field should contain gmail otherwise it will show validation error
   
    Password field should contain atleast 6 characters otherwise it will show validation error
   
    Rpassword field should matches with password field otherwise it will show validation error
   
    Feedback field should contain atleast 15 characters otherwise it will show validation error
   
#. Define view function inside views.py
   Post method is used inside function
   
#. Define view function inside urls.py

#. To run server

    py manage.py runserver







   


