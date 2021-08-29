# E-Lapor-PSU

## Install Guide
1. Create virtual environment by typing ``` virtualenv ENVIRONMENT_NAME ``` on the cmd

2. Activate the virtual environment by using ``` ENVIRONMENT_NAME\scripts\activate ```

3. Install the neccessary dependencies (Django, Pillow, MySQLClient)
```
python -m pip install Django
python -m pip install Pillow
python -m pip install mysqlclient
```

4. Go to e_lapor_psu folder ``` cd e_lapor_psu ```

5. Open xampp first, then open phpmyadmin and create e-lapor-psu database on ``` localhost/phpmyadmin ```

6. Migrate data to the database using ``` python manage.py migrate ```

7. Create superuser to be the first admin using ``` python manage.py createsuperuser ```. More admin can be created by using this admin account.

8. Run the development server simply by typing ``` python manage.py runserver ```

