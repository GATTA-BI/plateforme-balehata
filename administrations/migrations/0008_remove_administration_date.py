# Generated by Django 4.1.5 on 2023-01-28 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrations', '0007_alter_administration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administration',
            name='date',
        ),
    ]
