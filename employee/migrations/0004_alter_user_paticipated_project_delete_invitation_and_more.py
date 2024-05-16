# Generated by Django 5.0.4 on 2024-05-16 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_remove_invitation_invited_by_and_more'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='paticipated_project',
            field=models.ManyToManyField(blank=True, to='project.project'),
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]