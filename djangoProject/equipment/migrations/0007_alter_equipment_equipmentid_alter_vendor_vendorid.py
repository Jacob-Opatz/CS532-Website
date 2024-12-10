# Generated by Django 5.1.1 on 2024-12-10 08:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("equipment", "0006_alter_maintenance_maintenanceid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="equipmentid",
            field=models.AutoField(
                db_column="EquipmentID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="vendorid",
            field=models.AutoField(
                db_column="VendorID", primary_key=True, serialize=False
            ),
        ),
    ]
