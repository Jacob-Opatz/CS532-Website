# Generated by Django 5.1.3 on 2024-12-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_remove_billing_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='phone',
            field=models.CharField(default=1234564567, max_length=20),
            preserve_default=False,
        ),
    ]
