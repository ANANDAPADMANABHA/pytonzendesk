# Generated by Django 4.1.2 on 2022-10-13 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0005_alter_department_description_alter_department_name'),
        ('authentication', '0005_alter_useraccount_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admins.department'),
        ),
    ]