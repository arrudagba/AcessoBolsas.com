# Generated by Django 4.2.11 on 2024-05-13 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institution', '0003_institution_checked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(help_text='Título da bolsa', max_length=150)),
                ('tipoBolsa', models.CharField(help_text='Tipo da bolsa', max_length=100)),
                ('descricao', models.TextField(help_text='Descrição da bolsa', max_length=5000)),
                ('dataPostada', models.DateField(auto_now_add=True, help_text='Data da postagem da bolsa', verbose_name='Data da postagem')),
                ('dataAtualizada', models.DateField(auto_now=True, help_text='Data da atualização da bolsa', verbose_name='Data da atualização')),
                ('fotoPerfil', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='perfil_usuario')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.institution')),
            ],
        ),
    ]
