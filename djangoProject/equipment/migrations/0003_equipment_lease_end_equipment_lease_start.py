# Generated by Django 5.1.2 on 2024-12-06 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_equipment_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='lease_end',
            field=models.DateField(blank=True, db_column='LeaseEnd', null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='lease_start',
            field=models.DateField(blank=True, db_column='LeaseStart', null=True),
        ),
    ]