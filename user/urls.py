from django.urls import path
from . import views

app_name = 'user'          # 템플릿 작성할 때 사용하기 위해 app_name 지정

urlpatterns = [
    path('sign-in/', views.sign_in_view, name = 'sign-in'),
    path('sign-up/', views.sign_up_view, name = 'sign-up'),
    path('logout/', views.logout, name = 'logout')
]
