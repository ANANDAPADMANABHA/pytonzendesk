# Generated by Django 4.1.2 on 2022-10-16 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_useraccount_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='phone_number',
        ),
    ]
