# Generated by Django 2.2.4 on 2021-09-23 21:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Birthday',
            field=models.DateField(default=datetime.date(2021, 9, 24)),
        ),
    ]
