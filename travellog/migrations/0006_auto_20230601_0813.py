# Generated by Django 3.2.19 on 2023-06-01 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travellog', '0005_alter_logentry_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logentry',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
