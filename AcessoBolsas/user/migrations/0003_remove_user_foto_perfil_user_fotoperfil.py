# Generated by Django 4.2.11 on 2024-05-13 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_foto_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='foto_perfil',
        ),
        migrations.AddField(
            model_name='user',
            name='fotoPerfil',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='perfil_usuario'),
        ),
    ]
