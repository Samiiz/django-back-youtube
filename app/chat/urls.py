from django.urls import path
from .views import ChatRoomList, ChatMessageDetail, ChatRoomDetail

urlpatterns = [
    path('room', ChatRoomList.as_view(), name='room-list'),
    path('<int:room_id>/message', ChatMessageDetail.as_view(), name='messages'),
    path('<int:room_id>/roomdetail', ChatRoomDetail.as_view(), name='room-detail'),
]