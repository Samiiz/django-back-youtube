from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Video
from .serializers import VideoSerializer

# 전체 비디오정보를 불어오는 api
class Videolist(APIView):
    def get(self, request):
        videos = Video.objects.all()

        serializer = VideoSerializer(videos, many=True)

        return Response(serializer.data)

    def post():
        pass

# 특정 비디오에 대한 상세정보를 불러오는 api
class VideoDetail(APIView):
    # 먼저 get_object로 특정 pk에 해당하는 비디오를 불러온다
    def get_object(self, pk):
        # return get_object_or_404(Video, pk=pk)
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound
    # 불러온 get_object를 이용하여 VideoSerializer를 이용해 직렬화 한다
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