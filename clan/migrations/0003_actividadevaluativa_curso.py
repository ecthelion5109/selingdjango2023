# Generated by Django 4.2.4 on 2023-09-08 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clan', '0002_curso_escuela'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividadevaluativa',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clan.curso'),
        ),
    ]
