# Generated by Django 4.1.4 on 2023-01-23 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_user_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Id_no',
            field=models.CharField(default='kk', max_length=200),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='Role',
            field=models.ForeignKey(blank=True, default='student', null=True, on_delete=django.db.models.deletion.CASCADE, to='account.role'),
        ),
    ]