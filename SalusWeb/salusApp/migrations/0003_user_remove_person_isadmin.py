# Generated by Django 4.0.4 on 2022-04-16 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salusApp', '0002_remove_patient_person_patient_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='isAdmin',
        ),
    ]