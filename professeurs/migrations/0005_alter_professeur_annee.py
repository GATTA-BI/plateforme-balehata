# Generated by Django 4.1.5 on 2023-01-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professeurs', '0004_rename_date_creation_professeur_annee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professeur',
            name='annee',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
