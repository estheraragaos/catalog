# Catalog

## About the project

    This is a simple python back-end project to control e-commerce product catalog. 
## Libs

- [`Django`](https://docs.djangoproject.com)
- [`DjangoRestFramework`](https://www.django-rest-framework.org/)
- [`Psycopg2`](https://pypi.org/project/psycopg2/)
## Setup  

### Django run

Create a virtualenv named venv and active it

```
# create
$ python3 -m venv venv
# active
$ source/bin/activate
```

Install requirements

```
$ pip install -r requirements.txt
```

Migrate

```
$ python manage.py migrate
```

Run

```
$ python manage.py runserver
```