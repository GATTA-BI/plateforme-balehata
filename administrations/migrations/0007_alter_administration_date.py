# Generated by Django 4.1.5 on 2023-01-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrations', '0006_remove_administration_emargement_administration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
