# Generated by Django 3.1.14 on 2022-03-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0021_auto_20220304_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='location',
            field=models.CharField(choices=[('UZB', "O'zbekistondan Germaniyaga"), ('GER', "Germaniyadan O'zbekistonga"), ('UZBUSA', "O'zbekistondan Amerikaga"), ('USAUZB', "Amerikadan O'zbekistonga"), ('JPYUZB', "Yaponiyadan O'zbekistonga"), ('UZBJPY', "O'zbekistondan Yaponiyaga"), ('KORUZB', "Koreyadan O'zbekistondan"), ('UZBKOR', "O'zbekistondan Koreyaga"), ('TURUZB', "Turkiyadan O'zbekistonga"), ('UZBTUR', "O'zbekistondan Turkiyaga")], max_length=100, verbose_name='Pul yuboriladigan davlatni tanlang'),
        ),
    ]