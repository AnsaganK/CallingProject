# Generated by Django 3.1.7 on 2021-07-22 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210722_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='complaints_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]