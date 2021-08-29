# E-Lapor-PSU

This is a one of the core feature of the project for "E-Pengelolaan Aset Prasarana, Sarana dan Utilitas (PSU) Perumahan Berbasis Web di Kabupaten Sidoarjo". 
This feature focuses on checking the input data from "Pengembang" by the admin. If the admin finds a problem with the input, admin can send notifications to "Pengembang" so that they can fix the input. Those data includes:
* Data Perusahaan
* Data Proyek
* Data Perizinan
* Jenis PSU

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

