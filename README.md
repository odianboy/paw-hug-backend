# Intro
<hr />

Backend part for Paw Hug site.
# Installation
<hr />

Copy `.env.example` to `.env` and fill variables

This is just web application, so you need:

1. python >= 3.9
2. postgres >= 13

# Manual
<hr />

1. Create virtual environment
```
    1.1 pip install virtualenv
    1.2 python -m venv pawhugvenv
    1.3 pawhugvenv\Scripts\activate
```
2. Installing dependencies
<hr />

```
    2.1 pip install -r requirements.txt
```
3. Create database
<hr />

```sql
    # create user pawhug with password 'pawhug';
    # create database pawhug owner pawhug;
```

4. Migrate database:
```
    4.1 python manage.py migrate
    4.2 python manage.py createsuperuser
```
