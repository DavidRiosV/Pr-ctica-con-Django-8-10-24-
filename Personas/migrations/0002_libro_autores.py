# Generated by Django 5.1.1 on 2024-10-08 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(to='Personas.autor'),
        ),
    ]
