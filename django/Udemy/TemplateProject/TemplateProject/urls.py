from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template_app/', include('TemplateApp.urls'))
]
