# Generated by Django 4.2.4 on 2023-09-01 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliaProfesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.partido')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('lastname', models.CharField(max_length=255, null=True)),
                ('nacimiento', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.curso')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='familia_profesional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.familiaprofesional'),
        ),
        migrations.AddField(
            model_name='curso',
            name='institucion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.institucion'),
        ),
    ]
