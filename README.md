# Template for Django project



## 1. Introduction
The Django template is used for building a web application based on Python.
Software engineers might as well build their own web applications based on this template.

### 1.1 Design

- Web interface: Django4 
- Database: Sqlite3 or MySQL
- HTTP server: NGINX
- Cache(optional): Redis
- Asynchronous task: Celery
- UI design: Bootstrap5
- Front-end(optional): Vue-JS 
- Data analysis: Python3
- Deployment: Docker container

### 1.2 Features are showed as the below
- UI template: login/logout, example home page and navigation page, etc. 
- Authentication: Django user login and third-party login
- Authorization: custom user model, permissions on views
- APP: an example app known as reporting
- Task execution: Asynchronous and scheduled celery tasks
- RestFull APIs
- Continous integration: create image in github; run tests

## 2. Development

### 2.1 local devlopment 

#### Basic steps
Let's say a new project is named as "myapp"

install and build virtual environments
```
git clone git@github.com:Tiezhengyuan/django_template.git myapp
cd myapp
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then Run server locally. A administration user could be created.
```
python3 back_web/mange.py makemigrations accounts
python3 back_web/mange.py migrate
python3 back_web/mange.py createsuperuser
python3 back_web/mange.py runserver
```

#### Additional steps
Those steps below are optional depending on your requirements.

Run Redis
```
docker pull redis
docker run -it --rm --name redis -p 6379:6379 redis
```

Run celery tasks if redis is launched already.
```
cd back_web
celery -A back_web worker -l INFO
```

#### Access application in browser.

The web application could be accessed by http://127.0.0.1:8000/ in Google Chrome or other browsers.



### 2.2 container engine

To delete all containers including its volumes use,
```
docker rm -vf $(docker ps -aq)
docker rm <image id>
```

To delete all the images,
```
docker rmi -f $(docker images -aq)
```

Build image and run the app with docker container
```
docker compose up --build
```




### 2.3 Test APP in testing server

#### Build image and run the app with docker container
```
git clone git@github.com:Tiezhengyuan/django_template.git
cd django_template
podman-compose -f docker-compose-dev.yml up --build
```



### 2.4 Deploy APP in production server

#### Build image and run the app with docker container
```
git clone git@github.com:Tiezhengyuan/django_template.git
cd django_template
podman-compose -f docker-compose-prod.yml up --build -d
```
