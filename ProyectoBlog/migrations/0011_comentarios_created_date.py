# Generated by Django 4.1.1 on 2022-10-19 22:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoBlog', '0010_remove_comentarios_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
