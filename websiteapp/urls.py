from django.urls import path
from . import views

urlpatterns=[
    path('',views.mainfun,name='mainfun'),
    path('newfun/<int:cardid>',views.newfun,name='newfun'),
    path('searching',views.searching,name='searching'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    

]