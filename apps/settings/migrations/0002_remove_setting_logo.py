# Generated by Django 4.0.4 on 2022-04-30 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='logo',
        ),
    ]