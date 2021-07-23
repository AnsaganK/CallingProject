# Generated by Django 3.1.4 on 2021-07-23 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0021_auto_20210723_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_check_lists', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='IIN',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]