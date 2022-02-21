# Generated by Django 3.2.7 on 2022-02-21 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
            ],
        ),
    ]
