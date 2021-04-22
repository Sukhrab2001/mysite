from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.user_login, name="login" ),
    path('logout/', views.user_logout),
    path('registration/', views.user_registration, name="registration"),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view())
]