# Generated by Django 4.2 on 2023-09-22 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_alter_film_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='main_image',
            field=models.ImageField(upload_to='media/img/%Y/%m/%d/'),
        ),
    ]