# Generated by Django 4.1.6 on 2023-03-06 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDean', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentDean.block'),
        ),
        migrations.AlterField(
            model_name='placement',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentDean.dorm'),
        ),
    ]
