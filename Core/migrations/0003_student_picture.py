# Generated by Django 4.0.4 on 2022-04-29 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20220430_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(default=None, upload_to='student'),
            preserve_default=False,
        ),
    ]
