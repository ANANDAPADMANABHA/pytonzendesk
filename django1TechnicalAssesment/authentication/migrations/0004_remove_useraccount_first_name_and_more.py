# Generated by Django 4.1.2 on 2022-10-05 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_useraccount_department_useraccount_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
    ]
