# Generated by Django 3.2.5 on 2021-08-15 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20210815_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]