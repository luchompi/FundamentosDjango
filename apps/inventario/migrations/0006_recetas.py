# Generated by Django 5.0.2 on 2024-02-29 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_ingredientes_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(error_messages={'unique': 'La receta ya fue creada'}, max_length=150, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
