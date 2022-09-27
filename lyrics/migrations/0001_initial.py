# Generated by Django 4.1.1 on 2022-09-26 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.IntegerField()),
                ('nacionalidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('genero_musical', models.CharField(max_length=200)),
                ('duracao_seg', models.IntegerField()),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lyrics.artist')),
            ],
        ),
    ]
