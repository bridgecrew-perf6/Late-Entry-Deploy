# Generated by Django 4.0.4 on 2022-05-21 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='venue',
        ),
    ]
