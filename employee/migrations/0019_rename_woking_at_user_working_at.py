# Generated by Django 5.0.4 on 2024-05-20 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_user_woking_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='woking_at',
            new_name='working_at',
        ),
    ]
