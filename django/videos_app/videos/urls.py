from django.urls import path
from . import views
from .views import goodfunc, badfunc
app_name = 'videos'

urlpatterns = [
    path('', views.VideoList.as_view(), name='video_list'),
    path('create/', views.VideoCreate.as_view(), name='video_create'),
    path('update/<int:pk>', views.VideoUpdate.as_view(), name='video_update'),
    path('delete/<int:pk>', views.VideoDelete.as_view(), name='video_delete'),
    path('play/<int:pk>', views.VideoDetail.as_view(), name='video_detail'),
    path('comment/<int:pk>', views.CommentCreate.as_view(), name='comment_create'),
    path('category/<int:pk>/', views.VideoCategoryList.as_view(), name='video_category_list'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('good/<int:pk>',goodfunc, name='good'),
    path('bad/<int:pk>', badfunc, name='bad'),
]