# Generated by Django 3.1.14 on 2022-02-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20220227_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
