# Generated by Django 4.2.13 on 2024-05-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PCbuildingapp", "0002_alter_cpu_options_alter_gpu_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="f_name",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Vardas"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="l_name",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Vardas"
            ),
        ),
    ]