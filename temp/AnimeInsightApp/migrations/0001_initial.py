# Generated by Django 5.0.4 on 2024-05-05 07:15

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeMetadata',
            fields=[
                ('anime_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Name', max_length=200)),
                ('english_name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='English_name', max_length=200, null=True)),
                ('score', models.FloatField(blank=True, db_column='Score', null=True)),
                ('genres', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Genres', max_length=100, null=True)),
                ('synopsis', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Synopsis')),
                ('type', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Type', max_length=50, null=True)),
                ('episodes', models.SmallIntegerField(blank=True, db_column='Episodes', null=True)),
                ('aired', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Aired', max_length=50)),
                ('premiered', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Premiered', max_length=50, null=True)),
                ('status', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Status', max_length=50)),
                ('producers', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Producers', max_length=1550, null=True)),
                ('licensors', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Licensors', max_length=100, null=True)),
                ('studios', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Studios', max_length=200, null=True)),
                ('source', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Source', max_length=50, null=True)),
                ('duration', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Duration', max_length=50, null=True)),
                ('age_rating', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Age_Rating', max_length=50, null=True)),
                ('rank', models.IntegerField(blank=True, db_column='Rank', null=True)),
                ('scored_by', models.IntegerField(blank=True, db_column='Scored_By', null=True)),
                ('image_url', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Image_URL', max_length=100)),
            ],
            options={
                'db_table': 'Anime_Metadata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Historywatch',
            fields=[
                ('userid', models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'historywatch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('userid', models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('userid', models.OneToOneField(db_column='userID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'recommendation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('userid', models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('animename', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='AnimeName', max_length=50)),
            ],
            options={
                'db_table': 'request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('userid', models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'wishlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('userid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dob', models.DateField(null=True)),
                ('registered', models.BooleanField(default=False)),
            ],
        ),
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
