# Generated by Django 3.1.14 on 2022-02-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220226_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
