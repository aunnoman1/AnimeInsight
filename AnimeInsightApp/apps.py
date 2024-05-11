from django.apps import AppConfig
# from .signals import *
# from .models import FavGenres

class AnimeinsightappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AnimeInsightApp'

    # def ready(self):
    #     post_save.connect(recommend_anime_on_save, sender=FavGenres)