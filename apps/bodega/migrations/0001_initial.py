# Generated by Django 3.0.8 on 2022-07-07 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pieza', models.CharField(blank=True, max_length=10)),
                ('serie_pieza', models.CharField(blank=True, max_length=30)),
                ('descripcion_pieza', models.CharField(blank=True, max_length=40)),
                ('cantidad_pieza', models.IntegerField(blank=True)),
                ('fecha_pieza', models.DateField(auto_now_add=True)),
            ],
        ),
    ]