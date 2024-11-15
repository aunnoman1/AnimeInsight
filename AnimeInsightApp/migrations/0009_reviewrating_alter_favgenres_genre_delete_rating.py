# Generated by Django 5.0.4 on 2024-05-17 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnimeInsightApp', '0008_profile_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('rev', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
            ],
            options={
                'db_table': 'review_rating',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='favgenres',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Avant Garde', 'Avant Garde'), ('Award Winning', 'Award Winning'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Gourmet', 'Gourmet'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Slice of Life', 'Slice of Life'), ('Sports', 'Sports'), ('Supernatural', 'Supernatural'), ('Suspense', 'Suspense')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
