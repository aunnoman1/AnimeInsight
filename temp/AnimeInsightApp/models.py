from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



class AnimeMetadata(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    english_name = models.CharField(db_column='English_name', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    genres = models.CharField(db_column='Genres', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    synopsis = models.TextField(db_column='Synopsis', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    episodes = models.SmallIntegerField(db_column='Episodes', blank=True, null=True)  # Field name made lowercase.
    aired = models.CharField(db_column='Aired', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    premiered = models.CharField(db_column='Premiered', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    producers = models.CharField(db_column='Producers', max_length=1550, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    licensors = models.CharField(db_column='Licensors', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    studios = models.CharField(db_column='Studios', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age_rating = models.CharField(db_column='Age_Rating', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    scored_by = models.IntegerField(db_column='Scored_By', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='Image_URL', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime_Metadata'



class Historywatch(models.Model):
    userid = models.ForeignKey(User, models.CASCADE, db_column='userID', primary_key=True)  # Field name made lowercase. The composite primary key (userID, AnimeID) found, that is not supported. The first column is selected.
    animeid = models.ForeignKey(AnimeMetadata, models.CASCADE, db_column='AnimeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'historywatch'
        unique_together = (('userid', 'animeid'),)


class Rating(models.Model):
    userid = models.ForeignKey(User, models.CASCADE, db_column='userID', primary_key=True)  # Field name made lowercase. The composite primary key (userID, AnimeID) found, that is not supported. The first column is selected.
    animeid = models.ForeignKey(AnimeMetadata, models.CASCADE, db_column='AnimeID')  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'
        unique_together = (('userid', 'animeid'),)


class Recommendation(models.Model):
    userid = models.OneToOneField(User, models.CASCADE, db_column='userID', primary_key=True)  # Field name made lowercase.
    animeid1 = models.ForeignKey(AnimeMetadata, models.CASCADE, db_column='AnimeID1', blank=True, null=True)  # Field name made lowercase.
    animeid2 = models.ForeignKey(AnimeMetadata, models.CASCADE, db_column='AnimeID2', related_name='recommendation_animeid2_set', blank=True, null=True)  # Field name made lowercase.
    animeid3 = models.ForeignKey(AnimeMetadata, models.CASCADE, db_column='AnimeID3', related_name='recommendation_animeid3_set', blank=True, null=True)  # Field name made lowercase.
    animeid4 = models.ForeignKey(AnimeMetadata, models.CASCADE, db_column='AnimeID4', related_name='recommendation_animeid4_set', blank=True, null=True)  # Field name made lowercase.
    animeid5 = models.ForeignKey(AnimeMetadata, models.CASCADE, db_column='AnimeID5', related_name='recommendation_animeid5_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recommendation'


class Wishlist(models.Model):
    userid = models.ForeignKey(User, models.CASCADE, db_column='userID', primary_key=True)  # Field name made lowercase. The composite primary key (userID, AnimeID) found, that is not supported. The first column is selected.
    animeid = models.ForeignKey(AnimeMetadata, models.CASCADE, db_column='AnimeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wishlist'
        unique_together = (('userid', 'animeid'),)

class Request(models.Model):
    userid = models.ForeignKey(User, models.CASCADE, db_column='userID', primary_key=True)  # Field name made lowercase.
    animename = models.CharField(db_column='AnimeName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'request'

class Profile(models.Model):
    userid=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    dob = models.DateField(null=True)
    registered = models.BooleanField(default=False)

class FavGenres(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    

    GENRE_CHOICES = [
        ("Action","Action"),
        ("Adventure","Adventure"),
        ("Avant Garde","Avant Garde"),
        ("Award Winning","Award Winning"),
        ("Boys Love","Boys Love"),
        ("Comedy","Comedy"),
        ("Drama","Drama"),
        ("Ecchi","Ecchi"),
        ("Erotica","Erotica"),
        ("Fantasy","Fantasy"),
        ("Girls Love","Girls Love"),
        ("Gourmet","Gourmet"),
        ("Hentai","Hentai"),
        ("Horror","Horror"),
        ("Mystery","Mystery"),
        ("Romance","Romance"),
        ("Sci-Fi","Sci-Fi"),
        ("Slice of Life","Slice of Life"),
        ("Sports","Sports"),
        ("Supernatural","Supernatural"),
        ("Suspense","Suspense"),
    ]

    genre=models.CharField(null=False,max_length=20,choices=GENRE_CHOICES)

    class Meta:
        unique_together=(('userid','genre'),)