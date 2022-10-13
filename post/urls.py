from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post-new/', views.post_new, name = 'post-new'),
    path('post-delete/<int:post_id>/', views.post_delete, name = 'post-delete'),
    path('post-update/<int:post_id>/', views.post_update, name = 'post-update'),
    path('comment-detail/<int:post_id>/', views.comment_detail, name = 'comment-detail'),
]

