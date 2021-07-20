# Generated by Django 3.1.7 on 2021-07-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210720_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='comment',
            new_name='comments',
        ),
        migrations.AddField(
            model_name='father',
            name='work_type',
            field=models.ManyToManyField(blank=True, null=True, to='app.WorkType'),
        ),
    ]
