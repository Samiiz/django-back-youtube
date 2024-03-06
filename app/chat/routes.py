from django.urls import re_path, path, include
from .consumers import ChatConsumer

websoket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_id>\d+)/chat/') # 정규 표현식 사용 예
    path('ws/chat/<int:room_id>/', ChatConsumer.as_asgi())
] 