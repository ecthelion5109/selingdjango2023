# Generated by Django 4.2.4 on 2023-09-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_alter_curso_slug_alter_estudiante_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]