from django.urls import path
from . import views

urlpatterns = [
    # 내가 만든거
    # path('', views.SubscriptionList.as_view(), name='sub-list'),
    # path('<int:pk>/', views.SubscriptionList.as_view(), name='sub'),
    # 수업
    path('', views.SubscriptionList.as_view(), name='subs-list'),
    path('<int:pk>/', views.SubscriptionDetail.as_view(), name='subs-detail'),
]