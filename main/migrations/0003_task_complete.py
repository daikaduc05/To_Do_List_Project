# Generated by Django 5.0.2 on 2024-03-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_task_id_alter_users_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
