# Generated by Django 3.1.14 on 2022-03-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0029_auto_20220323_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='location',
            field=models.CharField(choices=[('Uzbekistan', 'Uzbekistan'), ('Germany', 'Germany'), ('USA', 'USA')], max_length=50, verbose_name='Pul yuboriladigan davlatni tanlang'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='whichLocation',
            field=models.CharField(choices=[('Toshkent viloyati', 'Toshkent viloyati'), ("Farg'ona vodiysi", "Farg'ona vodiysi"), ('Samarqand', 'Samarqand'), ("Farg'ona", "Farg'ona"), ('Namangan', 'Namangan'), ('Andijon', 'Andijon'), ('Guliston', 'Guliston'), ('Jizzax', 'Jizzax'), ('Qashqadaryo', 'Qashqadaryo'), ('Surxondaryo', 'Surxondaryo'), ('Navoiy', 'Navoiy'), ('Xorazm', 'Xorazm'), ('Buxoro', 'Buxoro'), ("Qoraqalpog'iston", "Qoraqalpog'iston"), ('Stadt München', 'Stadt München'), ('Stadt Berlin', 'Stadt Berlin'), ('Stadt Hamburg', 'Stadt Hamburg'), ('Stadt Köln', 'Stadt Köln'), ('Stadt Frankfurt', 'Stadt Frankfurt'), ('Bayern', 'Bayern'), ('Baden Württemberg', 'Baden Württemberg'), ('Bremen', 'Bremen'), ('Brandenburg', 'Brandenburg'), ('Hessen', 'Hessen'), ('Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern'), ('Niedersachsen', 'Niedersachsen'), ('Nordrhein Westfalen', 'Nordrhein Westfalen'), ('Rheinland Pfalz', 'Rheinland Pfalz'), ('Sachsen', 'Sachsen'), ('Sachsen-Anhalt', 'Sachsen-Anhalt'), ('Saarland', 'Saarland'), ('Schleswig Holstein', 'Schleswig Holstein'), ('Thüringen', 'Thüringen'), ('New York city', 'New York city'), ('Los Angeles', 'Los Angeles'), ('Chicago', 'Chicago'), ('Houston', 'Houston'), ('Phoenix', 'Phoenix'), ('Philadelphia', 'Philadelphia'), ('San Antonio', 'San Antonio'), ('San Diego', 'San Diego'), ('Dallas', 'Dallas'), ('San Jose', 'San Jose'), ('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('indiana', 'indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virgina', 'Virgina'), ('West Virgina', 'West Virgina')], max_length=50, verbose_name='Qaysi shahar yoki viloyat/Bundesland ga yubormoqchisiz'),
        ),
    ]
