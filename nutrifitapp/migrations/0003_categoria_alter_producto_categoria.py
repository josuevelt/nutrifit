# Generated by Django 4.0.6 on 2022-07-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrifitapp', '0002_producto_delete_suplemento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(default='sin categoría', max_length=255),
        ),
    ]
