# Generated by Django 3.1.14 on 2022-02-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='location',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
