# Generated by Django 4.0.4 on 2022-04-17 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salusApp', '0008_user_is_super'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
