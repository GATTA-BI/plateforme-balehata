# Generated by Django 2.2.12 on 2023-10-02 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emarge', '0004_rename_nombre_d_heures_emarge_nombre_d_heures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emarge',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
