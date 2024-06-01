# Generated by Django 5.0.6 on 2024-06-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to='school.teacher', verbose_name='Учителя'),
        ),
    ]
