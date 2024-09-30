# Generated by Django 5.1.1 on 2024-09-23 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0004_remove_alumno_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='semestre',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='asistencia',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='calificacion',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
