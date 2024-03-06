from rest_framework import serializers
from .models import ChatRoom, ChatMessage, ChatRoomMember

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
        read_only_fields = ['sender', 'room']

class ChatroomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomMember
        fields = '__all__'
        read_only_fields = ['user', 'room']