# Generated by Django 4.2.11 on 2024-06-03 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_last_login_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]