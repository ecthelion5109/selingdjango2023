# Generated by Django 4.2.4 on 2023-09-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_alter_curso_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]