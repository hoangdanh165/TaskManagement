# Generated by Django 5.0.4 on 2024-05-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user-avatars/'),
        ),
    ]
