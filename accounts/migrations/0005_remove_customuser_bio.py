# Generated by Django 3.1.14 on 2022-02-26 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='bio',
        ),
    ]
