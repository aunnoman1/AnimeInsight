from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Existing URL pattern
    path('add-to-wishlist/<int:anime_id>/', views.add_to_wishlist, name='add_to_wishlist'),  # New URL pattern
     path('wishlist/', views.view_wishlist, name='wishlist'),
     path('remove-from-wishlist/<int:anime_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
