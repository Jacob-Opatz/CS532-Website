# Generated by Django 5.1.2 on 2024-12-05 22:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipmentid', models.IntegerField(db_column='EquipmentID', primary_key=True, serialize=False)),
                ('type', models.CharField(db_column='Type', max_length=45)),
                ('lease_terms', models.CharField(blank=True, db_column='Lease Terms', max_length=45, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=120, null=True)),
                ('departmentleased', models.CharField(blank=True, db_column='DepartmentLeased', max_length=45, null=True)),
                ('owned_lease', models.CharField(db_column='Owned/Lease', max_length=1)),
                ('purchasedate', models.DateField(blank=True, db_column='PurchaseDate', null=True)),
                ('warenty_info', models.CharField(blank=True, db_column='Warenty Info', max_length=120, null=True)),
            ],
            options={
                'db_table': 'equipment_two',
            },
        ),
        migrations.CreateModel(
            name='ProblemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendorid', models.IntegerField(db_column='VendorID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField()),
                ('equipment_types', models.CharField(help_text='Comma-separated list of equipment types', max_length=200)),
                ('preferred', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('maintenanceid', models.IntegerField(db_column='MaintenanceID', primary_key=True, serialize=False)),
                ('type', models.CharField(db_column='Type', max_length=45)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=120, null=True)),
                ('status', models.CharField(db_column='Status', max_length=45)),
                ('resolution', models.CharField(blank=True, db_column='Resolution', max_length=120, null=True)),
                ('created_at', models.DateTimeField(db_column='CreatedAt', default=django.utils.timezone.now)),
                ('equipmentid', models.ForeignKey(db_column='EquipmentID', on_delete=django.db.models.deletion.DO_NOTHING, to='equipment.equipment')),
            ],
            options={
                'db_table': 'maintenance_two',
                'unique_together': {('maintenanceid', 'equipmentid')},
            },
        ),
    ]
