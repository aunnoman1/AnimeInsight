# Generated by Django 5.0.4 on 2024-05-02 19:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnimeInsightApp', '0004_remove_profile_id_alter_profile_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Avant Garde', 'Avant Garde'), ('Award Winning', 'Award Winning'), ('Boys Love', 'Boys Love'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Ecchi', 'Ecchi'), ('Erotica', 'Erotica'), ('Fantasy', 'Fantasy'), ('Girls Love', 'Girls Love'), ('Gourmet', 'Gourmet'), ('Hentai', 'Hentai'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Slice of Life', 'Slice of Life'), ('Sports', 'Sports'), ('Supernatural', 'Supernatural'), ('Suspense', 'Suspense')], max_length=20)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('userid', 'genre')},
            },
        ),
    ]