# Template for Django project



## Introduction
The Django template is used for building a web application based on Python.
Software engineers might as well build their own web applications based on this template.

### Design

- Web interface: Django4 
- Database: Sqlite3 or MySQL
- HTTP server: NGINX
- Cache(optional): Redis
- Asynchronous task: Celery
- UI design: Bootstrap5
- Front-end(optional): Vue-JS 
- Data analysis: Python3
- Deployment: Docker container

### Functions are showed as the below
- UI template: login/logout, example home page and navigation page, etc. 

- Authentication: Django user login and third-party login
- Authorization: custom user model, permissions on views
- APP: an example app known as reporting
- Asynchronous tasks: celery task
- RestFull APIs
- Configuration for Development:  environments, docker, images in github etc.

## Development

### local devlopment 
Let's say a new project is named as "myapp"

install and build virtual environments
```
git clone git@github.com:Tiezhengyuan/django_template.git myapp
cd myapp
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Run server locally. A administration user could be created.
```
python3 back_web/mange.py makemigrations accounts
python3 back_web/mange.py migrate
python3 back_web/mange.py createsuperuser
python3 back_web/mange.py runserver
```
The web application could be accessed by http://127.0.0.1:8000/.

#### Build image and run the app with docker container
```
docker compose up --build
```

### Test APP in testing server

#### Build image and run the app with docker container
```
docker compose -f docker-compose-dev.yml up --build
```


### Deploy APP in production server

#### Build image and run the app with docker container
```
docker compose -f docker-compose-prod.yml up --build
```
