from django.urls import path
from . import views
from reactions.views import ReactionDetail
from comments.views import CommentList

urlpatterns = [
    path('', views.Videolist.as_view(), name='video-list'),
    path('<int:pk>/', views.VideoDetail.as_view(), name='video-detail'),
    path('<int:pk>/reaction/', ReactionDetail.as_view(), name='video-reaction'),
    path('<int:pk>/comment/', CommentList.as_view(), name='video-comment'),
]