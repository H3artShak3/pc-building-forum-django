# Generated by Django 4.2.13 on 2024-06-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PCbuildingapp", "0012_alter_ram_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="advertisements",
            name="aprasymas",
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AddField(
            model_name="advertisements",
            name="tema",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]