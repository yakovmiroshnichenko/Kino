# Generated by Django 4.2 on 2023-09-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_film_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='type_2D',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='type_3D',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='type_IMAX',
            field=models.BooleanField(default=False),
        ),
    ]
