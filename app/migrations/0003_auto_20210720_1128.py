# Generated by Django 3.1.4 on 2021-07-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210719_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='manager',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='number_phone',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='picture',
        ),
        migrations.AddField(
            model_name='patient',
            name='before_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
