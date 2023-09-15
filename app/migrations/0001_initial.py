# Generated by Django 4.2.5 on 2023-09-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loai_tin', models.CharField(max_length=255)),
                ('gia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dien_tich', models.DecimalField(decimal_places=2, max_digits=10)),
                ('huong_nha', models.CharField(max_length=255)),
                ('huong_ban_cong', models.CharField(max_length=255)),
                ('phap_ly', models.CharField(max_length=255)),
                ('chieu_ngang', models.DecimalField(decimal_places=2, max_digits=10)),
                ('chieu_dai', models.DecimalField(decimal_places=2, max_digits=10)),
                ('so_phong_ngu', models.IntegerField()),
                ('so_phong_ve_sinh', models.IntegerField()),
                ('so_tang', models.IntegerField()),
                ('noi_that', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('dia_chi', models.CharField(max_length=255)),
                ('mo_ta', models.TextField()),
            ],
        ),
    ]
