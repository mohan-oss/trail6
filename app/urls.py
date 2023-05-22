from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('prediction/', views.predict, name='predict'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutusers, name='logout'),
    path('', views.register, name='register'),
   
    
]