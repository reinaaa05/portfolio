from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('home', views.home,name='home'),
    path('members',views.members,name='members'),
    path('members<int:id>',views.members,name='member'),
]