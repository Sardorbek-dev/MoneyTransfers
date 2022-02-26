# Generated by Django 3.1.14 on 2022-02-26 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Man'), ('female', 'Woman')], default=0, max_length=100),
            preserve_default=False,
        ),
    ]
