# Generated by Django 3.2.2 on 2023-02-13 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TipoEntidad',
            new_name='Categoria',
        ),
        migrations.RenameField(
            model_name='entidad',
            old_name='tipo_entidad',
            new_name='categoria',
        ),
        migrations.AlterField(
            model_name='registro',
            name='asiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.asiento'),
        ),
        migrations.AlterModelTable(
            name='categoria',
            table='categoria',
        ),
        migrations.CreateModel(
            name='Retenciones',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('valor', models.FloatField(default=0)),
                ('unidad', models.CharField(max_length=10)),
                ('ultima_modificacion', models.DateTimeField()),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.cuenta')),
            ],
            options={
                'db_table': 'retenciones',
            },
        ),
        migrations.CreateModel(
            name='CuentasAsociadas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cuenta_asociada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuena_asociada_set', to='registros.cuenta')),
                ('cuenta_asociente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuenta_asociente_set', to='registros.cuenta')),
            ],
            options={
                'db_table': 'cuentas_asociadas',
            },
        ),
    ]
