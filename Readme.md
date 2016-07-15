## Setup Instructions

1. Git Clone Repository
2. cd into repository
3. Setting up venv
```
virtualenv env
source env/bin/activate
pip install django
pip install djangorestframework
pip install pygments
``` 
4. Migrations
```python manage.py migrate```
5. Create a admin superuser
```python manage.py createsuperuser```