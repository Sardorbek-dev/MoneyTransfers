# Generated by Django 3.1.14 on 2022-03-29 23:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0026_profilefeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefeedback',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='feedback_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]