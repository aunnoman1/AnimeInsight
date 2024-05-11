from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'AnimeInsightApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('hi/', views.index, name='index'),# Existing URL pattern
    path('add-to-wishlist/<int:anime_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('login/', views.login_request, name='login_request'),
    path('remove-from-wishlist/<int:anime_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('register/', views.register, name='register'),
    path('clear-history/', views.clear_history, name='clear_history'),
    path('complete_profile/', views.complete_profile, name='complete_profile'),
    path('history/', views.view_history, name='view_history'),
    path('add-to-history/<int:anime_id>/', views.add_to_history, name='add_to_history'),
    path('logout/', views.logout_request, name='logout_request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
