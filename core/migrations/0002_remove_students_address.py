# Generated by Django 3.2.13 on 2022-06-15 03:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='address',
        ),
    ]