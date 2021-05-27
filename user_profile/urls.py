from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('cycles/', views.CycleList.as_view()),
    path('cycles/<int:pk>/', views.CycleDetail.as_view()),
    path('click/', views.callClick, name="click"),
    path('buyBoost/', views.buyBoost, name="buyBoost"),
    path('boosts/<int:mainCycle>/', views.BoostList.as_view()),
]
