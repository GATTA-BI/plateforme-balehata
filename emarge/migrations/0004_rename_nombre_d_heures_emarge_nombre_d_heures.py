# Generated by Django 4.1.5 on 2023-04-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emarge', '0003_emarge_nombre_d_heures'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emarge',
            old_name='Nombre_d_heures',
            new_name='nombre_d_heures',
        ),
    ]
