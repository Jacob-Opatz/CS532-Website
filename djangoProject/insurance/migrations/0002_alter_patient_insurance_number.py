# Generated by Django 5.1.1 on 2024-12-07 04:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("insurance", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="insurance_number",
            field=models.CharField(max_length=15),
        ),
    ]
