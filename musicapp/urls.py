from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("album/", include('album.urls', namespace='album')),
    #path('', home_page)

]
