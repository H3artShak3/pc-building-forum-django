# Generated by Django 4.2.13 on 2024-06-04 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("PCbuildingapp", "0017_alter_postaireview_content_advertisementreview"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ram",
            old_name="type",
            new_name="type_ram",
        ),
    ]
