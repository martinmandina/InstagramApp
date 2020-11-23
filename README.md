## InstaApp

#### Live link''
### Description:
* This is an django application that  allows uploads of images by a user to their profiles similar to the popular app [instagram](https://instagram.com)

### User BDD:
* Register to the application.
* Upload images to the application,
* Set up a personal profile
* Search for other users
* click on username to view profile

### Installation Technologies Required:
* Django
* Python
* Virtual environment
### TECHNOLOGIES:
* Python3
* postgresql
* Django
* Bootstrap4
* CSS
* Heroku
### DEPENDECIES(main):
* gunicorn
* Pillow
## SETUP & INSTALLATION INSTRUCTIONS:
 1. Ensure that Python3.6 is installed.
 2. Open Terminal.
 3. Change working directory to preffered location where you want to clone directory.
 4. Create a virtual environment on your working directory.
 5. Install django and its depedencies in your virtual environment.
 6. Open application on your browser by running python3 manage.py runserver

#### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'instaapp'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```

### Known Bugs
* With slow internet speeds deployment to heroku is not a given.
### AUTHOR:
* Martin Sila Mandina.
## CONTACT INFORMATION
* Martin Sila Mandina
* P.O. Box 70055 - 00400 Nairobi, Kenya
* Email: martinsmandina@gmail.com
* TEL:+254 722 675 630
* LICENSE
#### * Copyright (c) 2020 **Martin Mandina**