# important notes for Django projects

1. Open terminal and creat folder to store project
2. move to the respective folder(make sure that you are on the right location)
3. create a virtual environment(python -m venv venv)
4. after creating, activate virtual environment
    venv\Scripts\activate
5. install django(pip install django)
6. create the project(django-admin startproject config .)
7. create the structure for the project 
    -create static, templates, img, css, and js folders
    -create the .gitignore, README.md

#additonal notes
-all of the subcommands for django are going to be called followed by python manage.py
-ex. python manage.py runserver
-if we want to check the full list, we can run python manage.py
-to create an app we need to run "python manage.py startapp NAME_OF_THE_APP" (remember to change NAME_OF_THE_APP for the actual name)
-after a creation of an app make sure to create the urls.py file inside of the app(IF AND ONLY IF YOU'RE GOING TO CREATE VIEWS ON IT)
