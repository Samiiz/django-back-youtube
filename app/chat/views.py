from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatRoom, ChatMessage, ChatRoomMember
from .serializers import ChatRoomSerializer, ChatMessageSerializer, ChatroomDetailSerializer

# Create your views here.
class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        user_data = request.data

        serializer = ChatRoomSerializer(data=user_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChatRoomDetail(APIView):
    def get(self, request, room_id):
        room = get_object_or_404(ChatRoom, id=room_id)
        room_serializer = ChatRoomSerializer(room)
        members = ChatRoomMember.objects.filter(room=room)
        members_serializer = ChatroomDetailSerializer(members, many=True)

        data = {
            'name': room_serializer.data,
            'members': members_serializer.data
        }
        print("data = ", data)
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, room_id):
        room = get_object_or_404(ChatRoom, id=room_id)
        try:
            serializer = ChatroomDetailSerializer(user=request.user, room=room)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ChatMessageDetail(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)
        serializer = ChatMessageSerializer(messages, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        serializer = ChatMessageSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(room=chatroom, sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
