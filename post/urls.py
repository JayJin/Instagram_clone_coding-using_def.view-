from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post-new/', views.post_new, name = 'post-new'),
    path('post-delete/<int:post_id>/', views.post_delete, name = 'post-delete'),
    path('post-update/<int:post_id>/', views.post_update, name = 'post-update'),
    path('comment/detail/<int:id>/', views.comment_detail, name = 'comment-detail'),
    path('comment/write/<int:id>', views.comment_write, name="comment-write"),
    path('comment/delete/<int:id>', views.comment_delete, name="comment-delete"),
    path('comment/update/<int:id>', views.comment_update, name="comment-update"),
]

