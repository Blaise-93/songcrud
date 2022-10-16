from django.urls import path
from .views import (album_list,
                    album_detail, album_create,
                    album_update, album_delete,
                    navigation
                    )

app_name = 'albums'
urlpatterns = [
    path('', album_list, name='album-list'),
    path('', navigation.as_view(), name='navigation'),
    path('<int:pk>/', album_detail, name='album-detail'),
    path('<int:pk>/update/', album_update, name='album-update'),
    path('<int:pk>/delete/', album_delete, name='album-delete'),
    path('album_create/', album_create, name='album-create')



]
