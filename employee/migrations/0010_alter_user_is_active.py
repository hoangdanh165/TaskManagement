# Generated by Django 5.0.4 on 2024-05-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_alter_user_managers_alter_user_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]