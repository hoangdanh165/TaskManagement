# Generated by Django 5.0.4 on 2024-05-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_rename_woking_at_user_working_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(default='Software Engineer', max_length=100),
        ),
    ]
