# Generated by Django 2.1.5 on 2019-11-06 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0003_remove_employee_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='other_deductions',
        ),
    ]
