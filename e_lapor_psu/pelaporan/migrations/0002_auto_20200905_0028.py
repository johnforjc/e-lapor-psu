# Generated by Django 3.1 on 2020-09-04 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelaporan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifikasi',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 5, 0, 28, 18, 46769)),
        ),
    ]