# Generated by Django 4.2 on 2023-09-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='banner_image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cinema',
            name='logo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='main_image',
            field=models.ImageField(default='', upload_to='cinema/media/img'),
            preserve_default=False,
        ),
    ]