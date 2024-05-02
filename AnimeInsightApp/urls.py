from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'AnimeInsightApp'
urlpatterns = [
    path(route='',view=views.home,name='home')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

