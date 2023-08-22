# Generated by Django 4.2 on 2023-08-22 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery_seo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=7)),
                ('is_image', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BannerNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rotation_speed', models.CharField(choices=[('5000', '5s'), ('10000', '10s'), ('15000', '15s'), ('20000', '20s'), ('30000', '30s'), ('45000', '45s'), ('60000', '1m')], default='5000', max_length=10)),
                ('url', models.URLField()),
                ('active', models.BooleanField()),
                ('gallery', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.imagegallery')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('rotation_speed', models.CharField(choices=[('5000', '5s'), ('10000', '10s'), ('15000', '15s'), ('20000', '20s'), ('30000', '30s'), ('45000', '45s'), ('60000', '1m')], default='5000', max_length=10)),
                ('url', models.URLField()),
                ('active', models.BooleanField()),
                ('gallery', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.imagegallery')),
            ],
        ),
    ]
