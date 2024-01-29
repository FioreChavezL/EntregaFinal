# Generated by Django 5.0.1 on 2024-01-12 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=60)),
                ('nombreRL', models.CharField(max_length=60)),
                ('apellidoRL', models.CharField(max_length=60)),
                ('correo_empresa', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=60)),
                ('tienda', models.CharField(max_length=60)),
                ('pais', models.CharField(max_length=60)),
                ('provincia', models.CharField(max_length=60)),
                ('distrito', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
            ],
        ),
    ]
