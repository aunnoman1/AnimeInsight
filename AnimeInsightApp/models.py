from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    registration_completed = models.BooleanField(default=False)# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnimeinsightappCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    date_of_birth = models.DateField()
    registration_completed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'AnimeInsightApp_customuser'


class AnimeinsightappCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AnimeinsightappCustomuser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AnimeInsightApp_customuser_groups'
        unique_together = (('customuser', 'group'),)


class AnimeinsightappCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AnimeinsightappCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AnimeInsightApp_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class AnimeMetadata(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    english_name = models.CharField(db_column='English_name', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    genres = models.CharField(db_column='Genres', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    synopsis = models.TextField(db_column='Synopsis', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    episodes = models.IntegerField(db_column='Episodes', blank=True, null=True)  # Field name made lowercase.
    aired = models.CharField(db_column='Aired', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    premiered = models.CharField(db_column='Premiered', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    producers = models.CharField(db_column='Producers', max_length=1550, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    licensors = models.CharField(db_column='Licensors', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    studios = models.CharField(db_column='Studios', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rating = models.CharField(db_column='Rating', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    scored_by = models.IntegerField(db_column='Scored_By', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='Image_URL', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime_Metadata'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AnimeinsightappCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Historywatch(models.Model):
    userid = models.OneToOneField(AnimeinsightappCustomuser, models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase. The composite primary key (userID, AnimeID) found, that is not supported. The first column is selected.
    animeid = models.ForeignKey(AnimeMetadata, models.DO_NOTHING, db_column='AnimeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'historywatch'
        unique_together = (('userid', 'animeid'),)


class Rating(models.Model):
    userid = models.OneToOneField(AnimeinsightappCustomuser, models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase. The composite primary key (userID, AnimeID) found, that is not supported. The first column is selected.
    animeid = models.ForeignKey(AnimeMetadata, models.DO_NOTHING, db_column='AnimeID')  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'
        unique_together = (('userid', 'animeid'),)


class Recommendation(models.Model):
    userid = models.OneToOneField(AnimeinsightappCustomuser, models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase.
    animeid1 = models.ForeignKey(AnimeMetadata, models.DO_NOTHING, db_column='AnimeID1', blank=True, null=True)  # Field name made lowercase.
    animeid2 = models.ForeignKey(AnimeMetadata, models.DO_NOTHING, db_column='AnimeID2', related_name='recommendation_animeid2_set', blank=True, null=True)  # Field name made lowercase.
    animeid3 = models.ForeignKey(AnimeMetadata, models.DO_NOTHING, db_column='AnimeID3', related_name='recommendation_animeid3_set', blank=True, null=True)  # Field name made lowercase.
    animeid4 = models.ForeignKey(AnimeMetadata, models.DO_NOTHING, db_column='AnimeID4', related_name='recommendation_animeid4_set', blank=True, null=True)  # Field name made lowercase.
    animeid5 = models.ForeignKey(AnimeMetadata, models.DO_NOTHING, db_column='AnimeID5', related_name='recommendation_animeid5_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recommendation'


class Request(models.Model):
    userid = models.ForeignKey(AnimeinsightappCustomuser, models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    animename = models.CharField(db_column='AnimeName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'request'


class Wishlist(models.Model):
    userid = models.OneToOneField(AnimeinsightappCustomuser, models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase. The composite primary key (userID, AnimeID) found, that is not supported. The first column is selected.
    animeid = models.ForeignKey(AnimeMetadata, models.DO_NOTHING, db_column='AnimeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wishlist'
        unique_together = (('userid', 'animeid'),)
