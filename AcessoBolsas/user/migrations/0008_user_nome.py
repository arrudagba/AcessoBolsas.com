# Generated by Django 4.2.11 on 2024-06-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_user_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nome',
            field=models.CharField(default='namedefault', help_text='Informe o nome', max_length=100),
            preserve_default=False,
        ),
    ]