# Generated by Django 4.2.4 on 2023-09-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descripcion',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
