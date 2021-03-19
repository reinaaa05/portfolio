from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('detail/<int:pk>/', views.review_detail, name='review_detail'),
    path('create', views.review_create, name='review_create'),
    path('create/send/', views.review_create_send, name='review_create_send'),
  
]