# Generated by Django 4.0.4 on 2022-04-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salusApp', '0007_rename_staff_user_is_staff_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_super',
            field=models.BooleanField(default=False),
        ),
    ]