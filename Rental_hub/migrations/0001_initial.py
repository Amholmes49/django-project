# Generated by Django 3.0.5 on 2020-04-08 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('property_type', models.CharField(choices=[('Apartment', 'Apartment'), ('SFH', 'Single Family Home'), ('Duplex/Triplex/Townhouse', 'Duplex/Triplex/Townhouse'), ('Mobile/Manufactured', 'Mobile/Manufactured'), ('Commercial', 'Commercial')], default='SFH', max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField(max_length=20)),
                ('lease_start', models.DateField()),
                ('lease_end', models.DateField()),
                ('property_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tenants', to='Rental_hub.Property')),
            ],
        ),
    ]
