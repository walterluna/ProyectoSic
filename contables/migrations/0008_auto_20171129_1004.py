# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 16:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contables', '0007_balancegeneral'),
    ]

    operations = [
        migrations.CreateModel(
            name='CIF',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('dui', models.AutoField(primary_key=True, serialize=False)),
                ('nombreEmpleado', models.CharField(max_length=256)),
                ('apellidoEmpleado', models.CharField(max_length=256)),
                ('fecha', models.DateField(help_text='Formato: AAAA/MM/DD', verbose_name='Fecha de Contratacion')),
            ],
        ),
        migrations.CreateModel(
            name='empleadosXorden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dui', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaEntrada', models.DateField(help_text='Formato: AAAA/MM/DD', verbose_name='Fecha de Entrada')),
                ('cantidadEntrada', models.IntegerField()),
                ('costoTotalEntrada', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
                ('costoUnitarioEntrada', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
            ],
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='materialUtilizado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreMateriaPrima', models.CharField(max_length=256)),
                ('cantidad', models.IntegerField()),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=256)),
                ('CMOD', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
                ('cantEmpleados', models.IntegerField()),
                ('diasTrabajados', models.IntegerField()),
                ('fechaCreacion', models.DateField(help_text='Formato: AAAA/MM/DD', verbose_name='Fecha de Creacion')),
                ('fechaEntrega', models.DateField(help_text='Formato: AAAA/MM/DD', verbose_name='Fecha de Entrega')),
                ('CIF_O', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
                ('CMP', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
                ('cif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.CIF')),
            ],
        ),
        migrations.CreateModel(
            name='Pan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='planillaGeneral',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('AFP_general', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='AFP')),
                ('ISSS_general', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='ISSS')),
                ('salarioTotal', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='SalarioTotal')),
                ('vacaciones', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Vacaciones')),
                ('dui', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='productoTerminado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadProducto', models.IntegerField()),
                ('costoUnitarioProducto', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Costo Unitario')),
                ('costoTotalProducto', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
                ('orden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.Orden')),
            ],
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaSalida', models.DateField(help_text='Formato: AAAA/MM/DD', verbose_name='Fecha de Entrada')),
                ('cantidadSalida', models.IntegerField()),
                ('costoTotalSalida', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
                ('costoUnitarioSalida', models.DecimalField(decimal_places=2, max_digits=50, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='haber')),
                ('kardex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.Kardex')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='pan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.Pan'),
        ),
        migrations.AddField(
            model_name='materialutilizado',
            name='materiaPrima',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.MateriaPrima'),
        ),
        migrations.AddField(
            model_name='materialutilizado',
            name='orden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.Orden'),
        ),
        migrations.AddField(
            model_name='kardex',
            name='materiaPrima',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.MateriaPrima'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='kardex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.Kardex'),
        ),
        migrations.AddField(
            model_name='empleadosxorden',
            name='orden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contables.Orden'),
        ),
    ]