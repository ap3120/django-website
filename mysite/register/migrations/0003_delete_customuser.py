# Generated by Django 4.1.7 on 2023-03-22 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_customuser_todolists'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
