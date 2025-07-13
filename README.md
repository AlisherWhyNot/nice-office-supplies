
# nice office suppliers

Django project with API, stationary store project, you can whrite comments there.

## Installation

### clone this project
```bash
  git clone <thisproject>
```

### make venv
```bash
python -m venv venv
```

### activate venv
```bash
source venv/Scripts/activate
```
###### or (depends on your OS)
```bash
source venv/bin/activate
```

### install requirements
```bash
pip install -r requirements.txt
```
### migrate, runserver
```bash
cd stationery/
py manage.py migrate
py manage.py runserver
```
### load fixtures (optional) 
###### some categories, products and comments are here
```bash
python manage.py loaddata db.json 
```

## some endpoints
###### API documentation
http://127.0.0.1:8000/swagger/
###### ReDoc
http://127.0.0.1:8000/redoc/
###### main page
http://127.0.0.1:8000/
## Feedback

If you have any feedback, please reach out to us at doesnotexist@dontwritehereplz.com


## We recommend it
Install [Postman](https://www.postman.com/) to make requests in easier way.

## Features

- JWT authentication
- API exists in own app

## requirements.txt file contents
```txt
asgiref==3.9.0
certifi==2025.6.15
cffi==1.17.1
charset-normalizer==3.4.2
cryptography==45.0.5
defusedxml==0.7.1
Django==4.2.23
django-filter==25.1
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
djoser==2.3.1
drf-yasg==1.21.10
flake8==7.3.0
idna==3.10
inflection==0.5.1
isort==6.0.1
mccabe==0.7.0
oauthlib==3.3.1
packaging==25.0
pycodestyle==2.14.0
pycparser==2.22
pyflakes==3.4.0
PyJWT==2.9.0
python3-openid==3.2.0
pytz==2025.2
PyYAML==6.0.2
requests==2.32.4
requests-oauthlib==2.0.0
social-auth-app-django==5.4.3
social-auth-core==4.7.0
sqlparse==0.5.3
typing_extensions==4.14.1
tzdata==2025.2
uritemplate==4.2.0
urllib3==2.5.0
```
## Authors

- [@AlisherWhyNot](https://github.com/AlisherWhyNot)


## License

[Apache License](http://www.apache.org/licenses/)

