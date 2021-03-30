from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.VideoList.as_view(), name='video_list'),
    path('create/', views.VideoCreate.as_view(), name='video_create'),
    path('update/<int:pk>', views.VideoUpdate.as_view(), name='video_update'),
    path('delete/<int:pk>', views.VideoDelete.as_view(), name='video_delete'),
    path('play/<int:pk>', views.VideoDetail.as_view(), name='video_detail'),
    path('comment/<int:pk>', views.CommentCreate.as_view(), name='comment_create'),
]