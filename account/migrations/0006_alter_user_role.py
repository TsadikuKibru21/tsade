# Generated by Django 4.1.4 on 2023-01-12 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.role'),
        ),
    ]