# Generated by Django 4.2.13 on 2024-06-03 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PCbuildingapp", "0010_advertisements"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gpu",
            name="model",
            field=models.CharField(max_length=25, verbose_name="Modelis"),
        ),
    ]