# Generated by Django 3.2.2 on 2023-06-20 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_auto_20230620_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobante',
            name='link_comprobante',
            field=models.CharField(blank=True, default=None, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='tipocomprobante',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=60, null=True),
        ),
    ]