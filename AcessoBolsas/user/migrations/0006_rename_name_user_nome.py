# Generated by Django 4.2.11 on 2024-06-03 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nome',
        ),
    ]