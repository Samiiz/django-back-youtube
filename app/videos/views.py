from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

class Videolist(APIView):
    def get(self, request):
        videos = Video.objects.all()
        print('비디오 = ', videos)

        serializer = VideoSerializer(videos, many=True)

        return Response(serializer.data)

    def post():
        pass