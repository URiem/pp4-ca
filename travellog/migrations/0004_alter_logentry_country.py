# Generated by Django 3.2.19 on 2023-06-01 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travellog', '0003_auto_20230601_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travellog.country'),
        ),
    ]
