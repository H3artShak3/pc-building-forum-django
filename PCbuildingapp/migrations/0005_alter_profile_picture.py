# Generated by Django 4.2.13 on 2024-05-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PCbuildingapp", "0004_alter_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="picture",
            field=models.ImageField(
                default="default-user.png", upload_to="profile_pics"
            ),
        ),
    ]
