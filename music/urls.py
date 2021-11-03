from django.urls import path 
from . import views

urlpatterns = [
    path('home',views.home),
    path('camera', views.index,name='index'),
     
    path('video_feed', views.video_feed, name='video_feed'),#access the laptop camera
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),#access the mobile phone camera
]
