# Generated by Django 2.2.12 on 2023-10-02 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrations', '0008_remove_administration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
