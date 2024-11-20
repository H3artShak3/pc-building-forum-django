# Generated by Django 4.2.13 on 2024-05-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PCbuildingapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cpu",
            options={
                "verbose_name": "Procesorius",
                "verbose_name_plural": "Procesoriai",
            },
        ),
        migrations.AlterModelOptions(
            name="gpu",
            options={
                "verbose_name": "Vaizdo plokštė",
                "verbose_name_plural": "Vaizdo plokštės",
            },
        ),
        migrations.AlterModelOptions(
            name="postai",
            options={"verbose_name": "Postas", "verbose_name_plural": "Postai"},
        ),
        migrations.AlterModelOptions(
            name="ram",
            options={
                "verbose_name": "Ram atmintis",
                "verbose_name_plural": "Ram atmintys",
            },
        ),
        migrations.AlterModelOptions(
            name="userrig",
            options={
                "verbose_name": "Naudotojo kompiuteris",
                "verbose_name_plural": "Naudotojų kompiuteriai",
            },
        ),
        migrations.AddField(
            model_name="ram",
            name="size",
            field=models.IntegerField(null=True, verbose_name="Atminties dysis"),
        ),
        migrations.AlterField(
            model_name="postai",
            name="ft_1",
            field=models.ImageField(
                default="no_photo.jpg",
                upload_to="post_pics",
                verbose_name="Paveiksliukas Nr. 1",
            ),
        ),
        migrations.AlterField(
            model_name="postai",
            name="ft_2",
            field=models.ImageField(
                default="no_photo.jpg",
                upload_to="post_pics",
                verbose_name="Paveiksliukas Nr. 2",
            ),
        ),
        migrations.AlterField(
            model_name="postai",
            name="ft_3",
            field=models.ImageField(
                default="no_photo.jpg",
                upload_to="post_pics",
                verbose_name="Paveiksliukas Nr. 3",
            ),
        ),
        migrations.AlterField(
            model_name="postai",
            name="ft_4",
            field=models.ImageField(
                default="no_photo.jpg",
                upload_to="post_pics",
                verbose_name="Paveiksliukas Nr. 4",
            ),
        ),
        migrations.AlterField(
            model_name="postai",
            name="ft_5",
            field=models.ImageField(
                default="no_photo.jpg",
                upload_to="post_pics",
                verbose_name="Paveiksliukas Nr. 5",
            ),
        ),
    ]
