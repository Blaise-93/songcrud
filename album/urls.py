from django.urls import path
from .views import album_list, album_detail, album_create

app_name = 'album'
urlpatterns = [
    path('', album_list),
    path('<int:pk>/', album_detail),

    path('album_create/', album_create, name='album-create'),



]
