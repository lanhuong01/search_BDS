# Generated by Django 4.2.5 on 2023-09-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BDS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_type', models.TextField(choices=[('Mua bán', 'Mua bán'), ('Nhà đất bán', 'Nhà đất bán'), ('Cần bán', 'Cần bán')], max_length=50, verbose_name='Loại tin')),
                ('price', models.FloatField(verbose_name='Giá')),
                ('size', models.FloatField(verbose_name='Diện tích (mét vuông)')),
                ('direction', models.TextField(blank=True, choices=[('Đông', 'Đông'), ('Tây', 'Tây'), ('Nam', 'Nam'), ('Bắc', 'Bắc'), ('Đông Nam', 'Đông Nam'), ('Tây Nam', 'Tây Nam'), ('Đông Bắc', 'Đông Bắc'), ('Tây Bắc', 'Tây Bắc')], max_length=50, null=True, verbose_name='Hướng nhà')),
                ('balcony_direction', models.TextField(blank=True, choices=[('Đông', 'Đông'), ('Tây', 'Tây'), ('Nam', 'Nam'), ('Bắc', 'Bắc'), ('Đông Nam', 'Đông Nam'), ('Tây Nam', 'Tây Nam'), ('Đông Bắc', 'Đông Bắc'), ('Tây Bắc', 'Tây Bắc')], max_length=50, null=True, verbose_name='Hướng ban công')),
                ('legal', models.TextField(choices=[('Đã có sổ', 'Đã có sổ'), ('Đang chờ sổ', 'Đang chờ sổ'), ('Sổ hồng', 'Sổ hồng'), ('Sổ đỏ', 'Sổ đỏ'), ('Giấy tờ hợp lệ', 'Giấy tờ hợp lệ'), ('Hợp đồng mua bán', 'Hợp đồng mua bán'), ('Sổ đỏ/ Sổ hồng', 'Sổ đỏ/ Sổ hồng')], max_length=50, verbose_name='Giấy tờ pháp lý')),
                ('width', models.TextField(blank=True, null=True, verbose_name='Chiều ngang')),
                ('length', models.TextField(blank=True, null=True, verbose_name='Chiều dài')),
                ('bedrooms', models.TextField(blank=True, null=True, verbose_name='Số phòng ngủ')),
                ('toilets', models.TextField(blank=True, null=True, verbose_name='Số toilets')),
                ('floors', models.TextField(blank=True, null=True, verbose_name='Tầng')),
                ('furniture', models.TextField(max_length=200, verbose_name='Nội thất')),
                ('url', models.TextField(verbose_name='URL')),
                ('location', models.TextField(max_length=200, verbose_name='Địa chỉ')),
                ('description', models.TextField(verbose_name='Mô tả')),
                ('range_price', models.TextField(choices=[('Nhỏ hơn 500000000', 'Nhỏ hơn 500000000'), ('Từ 500000000 đến 1000000000', 'Từ 500000000 đến 1000000000'), ('Từ 1000000000 đến 5000000000', 'Từ 1000000000 đến 5000000000'), ('Lớn hơn 5000000000', 'Lớn hơn 5000000000')], default='Nhỏ hơn 500000000', verbose_name='Khoảng giá')),
                ('range_size', models.TextField(choices=[('Nhỏ hơn 50', 'Nhỏ hơn 50'), ('Từ 50 đến 100', 'Từ 50 đến 100'), ('Từ 100 đến 500', 'Từ 100 đến 500'), ('Lớn hơn 500', 'Lớn hơn 500')], default='Nhỏ hơn 50', verbose_name='Khoảng diện tích')),
                ('city', models.TextField(default='Unknown', max_length=200, verbose_name='Thành phố')),
            ],
        ),
    ]
