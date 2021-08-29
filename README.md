# Install Project Tutorial

1. Create virtual environment
```
virtualenv ENVIRONMENT_NAME
```

2. Activate the virtual environment
```
ENVIRONMENT_NAME\scripts\activate
```

3. Install django
```
python -m pip install Django
```

4. Install Pillow for ImageField
```
python -m pip install Pillow
```

5. Install mysqlclient
```
pip install mysqlclient
```

6. Go to e_lapor_psu folder
```
cd e_lapor_psu
```

7. Open phpmyadmin and create e-lapor-psu database

8. Migrate data to database
```
python manage.py migrate
```

9. Create superuser to be the first admin
```
python manage.py createsuperuser
```

10. Run the server
```
python manage.py runserver
```

