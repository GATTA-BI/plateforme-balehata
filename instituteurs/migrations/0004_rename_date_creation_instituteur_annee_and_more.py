# Generated by Django 4.1.5 on 2023-01-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteurs', '0003_remove_instituteur_matiere_instituteur_classe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instituteur',
            old_name='date_creation',
            new_name='annee',
        ),
        migrations.AddField(
            model_name='instituteur',
            name='telephone',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
