# Generated by Django 3.2.7 on 2021-10-04 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_junta_representante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junta',
            name='rut',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='representante',
            name='rut',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='representante',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]