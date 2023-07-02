from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('register/',views.UserRegister,name="register"),
    path('profile/<str:pk>/',views.UserProfile,name="user_profile"),
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),


path('delete_message/<str:pk>/',views.delete_message,name="delete_message"),
    path('create_room/',views.create_room,name="create_room"),
    path('update_room/<str:pk>/',views.update_room,name="update_room"),
     path('delete_room/<str:pk>/',views.delete_room,name="delete_room"),
     path('update_user/',views.update_user,name="update_user"),
     path('topics_page/',views.topics_page,name="topics_page"),
     path('activity_page/',views.activity_page,name="activity_page"),
]