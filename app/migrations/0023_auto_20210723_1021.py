# Generated by Django 3.1.4 on 2021-07-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20210723_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='comments',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
