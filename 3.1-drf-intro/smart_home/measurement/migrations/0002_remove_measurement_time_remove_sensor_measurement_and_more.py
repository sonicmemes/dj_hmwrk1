# Generated by Django 5.0.6 on 2024-06-09 06:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='time',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='measurement',
        ),
        migrations.AddField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
