# Generated by Django 3.1.14 on 2022-02-21 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0005_auto_20220222_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='pul_yuboriladigan_davlatni_tanlang',
            field=models.CharField(choices=[('UZB', "O'zbekistondan Germaniyaga"), ('GER', "Germaniyadan O'zbekistonga")], max_length=100),
        ),
    ]
