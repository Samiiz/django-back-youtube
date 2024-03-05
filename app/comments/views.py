from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Video
from .serializers import CommentSerializer

# Create your views here.
class CommentList(APIView):
    def post(self, request, pk):
        user_data = request.data
        try:
            serializer = CommentSerializer(data=user_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, Video=get_object_or_404(Video, id=pk))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)