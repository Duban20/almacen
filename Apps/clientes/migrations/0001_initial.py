# Generated by Django 5.0.6 on 2024-05-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(help_text='Ingrese el Nombre del Cliente', max_length=100)),
                ('direccionCliente', models.CharField(help_text='Ingrese la Direccion del Cliente', max_length=100)),
                ('telefonoCliente', models.CharField(help_text='Ingrese el Telefono del Cliente', max_length=12)),
                ('correoCliente', models.EmailField(help_text='Ingrese el Correo del Cliente', max_length=100)),
                ('passwordCliente', models.CharField(help_text='Ingrese el Password del Cliente', max_length=100)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
