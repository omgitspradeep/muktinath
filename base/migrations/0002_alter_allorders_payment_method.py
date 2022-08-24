# Generated by Django 4.0.6 on 2022-08-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allorders',
            name='payment_method',
            field=models.CharField(choices=[('Khalti', 'Khalti'), ('IME Pay', 'IME Pay'), ('Esewa', 'Esewa'), ('Local Bank', 'Local Bank')], default='Khalti', max_length=20),
        ),
    ]