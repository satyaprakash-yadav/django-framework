
#Qs. What is a scripting ?
# To handle and Manipulate any other thing like (we can use os library in python which gives access of your os to handle).

# MVT :- Model View Template

# Model is table or database.

# Template is html data or file.

# View is get request and give response.


# ---------------------------- MVT Architecture ----------------------------------
#
#
#   
#                                   get request    give resp   
#                        __         give response  _________    
# user |  --> request   |  |           _______    | model   |
#     /|\            |  |  | request  |       | / |_________|   Table or Database 
#               urls.py |  |_________`| View  |/  
#                   ____|UI|_________ |       |\   get req  
#                  | -- |  |`response |_______| \ __________ 
#  Filter or fetch | -- |  |                     | Template |  
#     (map urls)   | -- |  |                     |__________|   Html Data or File   
#                  |_--_|__|                       give resp
#                      
#               urls dispatching



# ----------------------------- Virtual Environment -------------------------------
#
#               
#           _____________
#          |  MyProject  |____ Outer Project Folder 
#          |_____________| 
#          _____________________________________
#         |   MyProject  |____Inner Project Fold|  
#         |______________|                      |
#         |       |                             |
#         |       |___  __init__.py             |    (behave Package as a understanding)
#         |       |                             |
#         |       |___  setting.py              |
#         |       |                             |    
#         |       |___  asgi                    |    (Default server)
#         |       |                             |
#         |       |___  wsgi                    |    (   server    )
#         |       |                             |
#         |       |___  urls.py                 |
#         |    manage.py                        |    
#         |_____________                        |
#         | My App      |____Application Folder |
#         |_____________|                       |
#         |       |                             |
#         |       |___ Model                    |
#         |       |                             |
#         |       |___ View.py                  |    
#         |_____________________________________|


# cmd prompt :-
# To create virtual enironment
# >>> virtualenv env

# To activate linux os / environment :-
# >>> source env/bin/activate

# First Dependency
# >>> pip3 install django

# To check latest version
# >>> django-admin --version

# linux
# >>> source env/bin/activate

# windows
# >>> env\scripts\activate

# step 2:- Install required dependency(library such as django)
# >>> pip install django

# step 3:- Create project
# >>> django-admin startproject MyProject
# >>> code .

# step 4:- Create Application
# >>> cd Myproject\
# >>> python manage.py startapp MyApp

# step 5:- Install Application
# Go to inner project folder open setting.py
# >>> python manage.py runserver

# step 6:- Define urls
# >>> www.python.org/
#      |___________|  rout      
#            |
#         domain

# step 7 :- To create default database
# >>> python manage.py makemigrations
# >>> python manage.py migrate

# step 8 :- To create default admin panel
# >>> python manage.py createsuperuser


# Django project directory structure 

# 1). __init__.py :- The folder which contain __init__.py file is considered as python package.

# 2). wsgi.py :- WSGI(Web Server Gateway Interface) is a specification that describes how a web server communicates
# with web applications, and how web application can be chained together to process one request. WSGI provided a
# standard for synchronous python apps.

# 3). setting.py :- This file contains all the information or data about project settings like database confi 
# infomation , template, installed application, validators, etc.

# 4). asgi.py :- ASGI(Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a
# standard interface between async-capable python web servers, frameworks, and applications.ASGI provides standard for 
# both asynchronous and synchronous apps.

# 5). manage.py :- It is automatically created in each django project. It is django's command-line utility also 
# sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project setting.py file.
# Generally when working on a single django project it's easier to use manage.py than django-admin.





    



























