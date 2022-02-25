# Generated by Django 3.1.14 on 2022-02-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0011_transfer_qaysi_shahar_yoki_viloyat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='qaysi_shahar_yoki_viloyat',
            field=models.CharField(choices=[('tashkent', 'Toshkent'), ('tashkent_city', 'Toshkent shahri'), ('valley', 'Vodiy'), ('samarqandandtashkent', 'Toshkent/Samarqand'), ('namangan', 'Namangan'), ('andijan', 'Andijon'), ('fergana', "Farg'ona"), ('guliston', 'Guliston'), ('jizzax', 'Jizzax'), ('qashqadaryo', 'Qashqadaryo'), ('surxondaryo', 'Surxondaryo'), ('samarqand', 'Samarqand'), ('navoiy', 'Navoiy'), ('buxoro', 'Buxoro'), ('xorazm', 'Xorazm'), ('qaraqalpogiston', 'Nordrhein Westfalen'), ('qaraqalpogiston', 'Bayern'), ('qaraqalpogiston', 'Baden Württemberg'), ('qaraqalpogiston', 'Niedersachsen'), ('qaraqalpogiston', 'Hessen'), ('qaraqalpogiston', 'Rheinland Pfalz'), ('qaraqalpogiston', 'Sachsen'), ('qaraqalpogiston', 'Berlin'), ('qaraqalpogiston', 'Schleswig Holstein'), ('qaraqalpogiston', 'Brandenburg'), ('qaraqalpogiston', 'Sachsen-Anhalt'), ('qaraqalpogiston', 'Thüringen'), ('qaraqalpogiston', 'Hamburg'), ('qaraqalpogiston', 'Mecklenburg-Vorpommern'), ('qaraqalpogiston', 'Saarland'), ('qaraqalpogiston', 'Bremen')], max_length=50),
        ),
    ]