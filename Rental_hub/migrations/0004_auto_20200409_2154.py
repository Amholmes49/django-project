# Generated by Django 3.0.5 on 2020-04-09 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rental_hub', '0003_auto_20200408_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='property_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenants', to='Rental_hub.Property'),
        ),
    ]
