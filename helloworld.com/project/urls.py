from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('diaries/', include('diaries.urls')),
    path('',include('myprofile.urls')),
]
