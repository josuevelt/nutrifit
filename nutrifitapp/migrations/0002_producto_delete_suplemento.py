# Generated by Django 4.0.6 on 2022-07-17 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrifitapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('precio', models.CharField(max_length=100)),
                ('cantidad_disponible', models.CharField(max_length=255)),
                ('arte_imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('categoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Suplemento',
        ),
    ]
