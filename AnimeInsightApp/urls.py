from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'AnimeInsightApp'
urlpatterns = [
    path(route='',view=views.home,name='home'),
    path(route='login/',view=views.login_request,name='login_request'),
    path(route='register/',view=views.register,name='register'),
    path(route='complete_profile/',view=views.complete_profile,name='complete_profile'),
    path(route='logout/',view=views.logout_request,name='logout_request')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

