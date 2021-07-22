# Generated by Django 3.1.7 on 2021-07-22 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210722_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Группа крови',
                'verbose_name_plural': 'Группы крови',
            },
        ),
        migrations.AlterField(
            model_name='checklist',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='check_lists', to='app.patient'),
        ),
        migrations.AlterField(
            model_name='father',
            name='blood_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bloodtypes'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bloodtypes'),
        ),
    ]
