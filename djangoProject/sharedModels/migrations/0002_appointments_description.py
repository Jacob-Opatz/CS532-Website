# Generated by Django 5.1.1 on 2024-12-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sharedModels", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointments",
            name="description",
            field=models.CharField(default="N/A", max_length=500),
        ),
    ]