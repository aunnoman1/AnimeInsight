# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import FavGenres, AnimeMetadata
# from .views import recommend_anime

# @receiver(post_save, sender=FavGenres)
# def recommend_anime_on_save(sender, instance, created, **kwargs):
#     if created:
#         recommend_anime(instance.user_id)