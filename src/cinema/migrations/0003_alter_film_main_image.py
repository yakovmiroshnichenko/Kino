# Generated by Django 4.2 on 2023-09-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_cinema_banner_image_cinema_logo_film_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='main_image',
            field=models.ImageField(upload_to='src/cinema/media/img'),
        ),
    ]
