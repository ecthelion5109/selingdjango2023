# Generated by Django 4.2.4 on 2023-09-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0011_alter_curso_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
