# Generated by Django 5.0.1 on 2024-01-12 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder3', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cliente',
            new_name='clientes1',
        ),
        migrations.RenameModel(
            old_name='proveedor',
            new_name='proveedores1',
        ),
        migrations.RenameModel(
            old_name='tienda',
            new_name='tiendas1',
        ),
    ]
