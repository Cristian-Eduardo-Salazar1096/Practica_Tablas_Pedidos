# Generated by Django 5.1.2 on 2024-11-18 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.FloatField()),
                ('cantidad', models.SmallIntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=20)),
                ('id_provedor', models.SmallIntegerField()),
            ],
        ),
    ]
