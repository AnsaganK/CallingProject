# Generated by Django 3.1.7 on 2021-07-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210720_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile_phone',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='Мобильный телефон'),
        ),
    ]
