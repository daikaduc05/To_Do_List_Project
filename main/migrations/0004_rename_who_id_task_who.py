# Generated by Django 5.0.2 on 2024-03-06 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_task_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='who_id',
            new_name='who',
        ),
    ]