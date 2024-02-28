from django.urls import path
from . import views

urlpatterns = [
    path('', views.Videolist.as_view(), name='video-list')
]