# Generated by Django 5.1 on 2024-11-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Provedor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provedores',
            name='Telefono',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='provedores',
            name='horario',
            field=models.CharField(max_length=100),
        ),
    ]
