# Generated by Django 4.2.19 on 2025-03-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/img/'),
        ),
    ]
