# Generated by Django 3.1.14 on 2022-02-26 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20220226_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
    ]
