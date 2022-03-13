# Generated by Django 3.1.14 on 2022-03-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0026_transfer_reputation_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='job',
            field=models.CharField(choices=[('Software Engineer', 'Software Engineer'), ('Data Scientist', 'Data Scientist'), ('Accountant', 'Accountant'), ('Financial Analyst', 'Financial Analyst')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='subject',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Business', 'Business')], default=0, max_length=50),
            preserve_default=False,
        ),
    ]
