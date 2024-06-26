# Generated by Django 5.0.3 on 2024-04-06 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonsoc', models.CharField(max_length=50)),
                ('cuit', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('stockact', models.IntegerField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.proveedor')),
            ],
        ),
    ]
