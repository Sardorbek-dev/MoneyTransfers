# Generated by Django 3.1.14 on 2022-02-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='telegram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]