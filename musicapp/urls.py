from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("albums/", include('album.urls', namespace='albums'))
    #path('', home_page)

]
