# Generated by Django 3.1.14 on 2022-03-06 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0023_transfer_exchangerate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='location',
            field=models.CharField(choices=[('UZB', "O'zbekistondan Germaniyaga"), ('GER', "Germaniyadan O'zbekistonga"), ('UZBUSA', "O'zbekistondan Amerikaga"), ('USAUZB', "Amerikadan O'zbekistonga"), ('JPYUZB', "Yaponiyadan O'zbekistonga"), ('UZBJPY', "O'zbekistondan Yaponiyaga"), ('KORUZB', "Koreyadan O'zbekistondan"), ('UZBKOR', "O'zbekistondan Koreyaga"), ('TURUZB', "Turkiyadan O'zbekistonga"), ('UZBTUR', "O'zbekistondan Turkiyaga"), ('FRAUZB', "Fransiyadan O'zbekistonga"), ('UZBFRA', "O'zbekistondan Fransiyaga"), ('SHWUZB', "Shvetsariyadan O'zbekistonga"), ('UZBSHW', "O'zbekistondan Shvetsariyaga"), ('UZBITA', "O'zbekistondan Italiyaga"), ('POLUZB', "Polshadan O'zbekistonga"), ('UZBPOL', "O'zbekistondan Polshaga"), ('CHEXUZB', "Chexiyadan O'zbekistonga"), ('UZBCHEX', "O'zbekistondan Chexiyaga"), ('CANUZB', "Canadadan O'zbekistonga"), ('UZBCAN', "O'zbekistondan Canadaga"), ('AUSTUZB', "Australiyadan O'zbekistonga"), ('UZBAUST', "O'zbekistondan Australiyaga"), ('AUSUZB', "Avstriyadan O'zbekistonga"), ('UZBAUS', "O'zbekistondan Avstriyaga")], max_length=100, verbose_name='Pul yuboriladigan davlatni tanlang'),
        ),
    ]
