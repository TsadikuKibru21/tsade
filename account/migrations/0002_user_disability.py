# Generated by Django 4.1.6 on 2023-03-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='disability',
            field=models.CharField(choices=[('disable', 'disable'), ('non_disable', 'disable')], default=3, max_length=200),
            preserve_default=False,
        ),
    ]
