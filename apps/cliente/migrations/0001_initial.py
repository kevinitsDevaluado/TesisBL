# Generated by Django 3.0.8 on 2022-06-07 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre1_cliente', models.CharField(blank=True, max_length=100, verbose_name='Primer Nombre')),
                ('nombre2_cliente', models.CharField(blank=True, max_length=100, verbose_name='Segundo Nombre')),
                ('apellido1_cliente', models.CharField(blank=True, max_length=100, verbose_name='Primer Apellido')),
                ('apellido2_cliente', models.CharField(blank=True, max_length=100, verbose_name='Segundo Apellido')),
                ('cedula_cliente', models.CharField(blank=True, max_length=10, verbose_name='Cédula')),
                ('telefono_cliente', models.CharField(blank=True, max_length=10, verbose_name='teléfono')),
                ('direccion_cliente', models.CharField(blank=True, max_length=80, verbose_name='Dirección')),
                ('email_cliente', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
            ],
        ),
    ]
