from django.urls import path
from .import views

urlpatterns = [
    path('app/', views.app ,name='app'),
    path('login/', views.user_login ,name='login'),
    path('myprofile/', views.myprofile ,name='myprofile'),
    path('updat_profile/', views.updat_profile ,name='updat_profile'),
    path('Sign_up/', views.Sign_up ,name='Sign_up'),
    path('<slug:slug>/', views.doctor_detail ,name='doctor_detail'),
    
]