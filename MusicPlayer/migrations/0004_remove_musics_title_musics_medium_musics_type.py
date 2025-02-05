# Generated by Django 5.1.4 on 2025-02-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MusicPlayer", "0003_alter_musics_musicfile_alter_musics_musicthumbnail"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="musics",
            name="title",
        ),
        migrations.AddField(
            model_name="musics",
            name="medium",
            field=models.CharField(default="Hindi", max_length=10),
        ),
        migrations.AddField(
            model_name="musics",
            name="type",
            field=models.CharField(default="Romantic", max_length=10),
        ),
    ]
