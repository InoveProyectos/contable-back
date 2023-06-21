# Generated by Django 3.2.2 on 2023-06-20 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_alter_registro_numero_operacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='comprobante',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='registros.comprobante'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='tipo_comprobante',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='registros.tipocomprobante'),
        ),
    ]