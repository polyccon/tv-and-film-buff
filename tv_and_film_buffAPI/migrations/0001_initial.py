# Generated by Django 4.0.4 on 2022-04-27 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('total_seasons', models.IntegerField(default=1)),
                ('seriesID', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('plot', models.CharField(max_length=255)),
                ('episode_number', models.IntegerField(default=1)),
                ('season_number', models.IntegerField(default=1)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Drama', 'Drama')], default='Action', max_length=22)),
                ('language', models.CharField(choices=[('English', 'English'), ('Greek', 'Greek'), ('Italian', 'Italian')], max_length=30)),
                ('imdbRating', models.FloatField()),
                ('poster', models.URLField()),
                ('imdbID', models.CharField(max_length=10, unique=True)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='tv_and_film_buffAPI.series')),
            ],
            options={
                'ordering': ('series',),
            },
        ),
    ]
