# Generated by Django 4.0.3 on 2022-04-17 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_students_bairro_students_cep_students_complemento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='gia',
            new_name='numero',
        ),
        migrations.RemoveField(
            model_name='students',
            name='unidade',
        ),
    ]
