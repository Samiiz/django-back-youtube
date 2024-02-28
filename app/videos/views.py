from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
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

class VideoDetail(APIView):
    def get_object(self, pk):
        # return get_object_or_404(Video, pk=pk)
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound
    def get(self, request, pk):
        video = self.get_object(pk)

        serializer = VideoSerializer(video)

        return Response(serializer.data)
    def post():
        pass
    def put():
        pass
    def delete():
        pass