# Generated by Django 3.2.7 on 2021-10-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211003_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='representante',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]
