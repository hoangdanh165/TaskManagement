# Generated by Django 5.0.4 on 2024-05-17 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_rename_paticipated_project_user_participated_projects_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]