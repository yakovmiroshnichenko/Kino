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
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=50)),
                ('coords', models.CharField(verbose_name=20)),
            ],
        ),
        migrations.CreateModel(
            name='OtherPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('gallery', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.imagegallery')),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.seo')),
            ],
        ),
        migrations.CreateModel(
            name='NewsPromotionPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('active', models.BooleanField(default=True)),
                ('gallery', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.imagegallery')),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.seo')),
            ],
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('phone1', models.CharField(max_length=19)),
                ('phone2', models.CharField(max_length=19)),
                ('seo_text', models.TextField()),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.seo')),
            ],
        ),
    ]
