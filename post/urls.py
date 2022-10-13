from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post-all/', views.post_all, name='post-all'),
    path('post-new/', views.post_new, name = 'post-new'),
]
