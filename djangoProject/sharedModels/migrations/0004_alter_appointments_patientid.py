# Generated by Django 5.1.1 on 2024-12-10 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sharedModels", "0003_alter_appointments_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointments",
            name="patientid",
            field=models.ForeignKey(
                blank=True,
                db_column="PatientID",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="sharedModels.patientrecord",
            ),
        ),
    ]
