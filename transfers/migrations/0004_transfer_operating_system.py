# Generated by Django 3.1.14 on 2022-02-21 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0003_auto_20220221_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='operating_system',
            field=models.CharField(choices=[('Euro', 'Euro10'), ('Dollor', 'Dollor20'), ('Söm', 'Söm20')], default=0, max_length=50),
            preserve_default=False,
        ),
    ]
