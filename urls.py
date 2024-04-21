from django.urls import path
from . import views
from .views import add_to_cart

urlpatterns = [
    path('', views.index, name='index'),  # This URL pattern is already defined
     path('add-to-cart/', add_to_cart, name='add_to_cart'),
       path('cart/', views.view_cart, name='view_cart'),
      path('empty-cart/', views.empty_cart, name='empty_cart'),
    path('anime/', views.index, name='anime_list'),  # Add this line for the anime list view
]
