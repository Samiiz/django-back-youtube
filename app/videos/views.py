from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer
from .managers import ReactionCustomManager
import pdb



# 전체 비디오정보를 불어오는 api
class Videolist(APIView):
    def get(self, request):
        videos = Video.objects.all()

        serializer = VideoSerializer(videos, many=True)

        return Response(serializer.data)

    def post(self, request):
        try:
            user_data = request.data
            serilaizer = VideoSerializer(data=user_data)

            if serilaizer.is_valid():
                serilaizer.save(user=request.user)
                return Response(serilaizer.data, status=status.HTTP_201_CREATED)
            return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)

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

        data = {
            'video': serializer.data,
            'likes' : ReactionCustomManager.GetLikes(pk),
            'dislikes' : ReactionCustomManager.GetDISLikes(pk)
        }

        return Response(data)
    def post():
        pass
    def put(self, request, pk):
        video = self.get_object(pk)

        try:
            serializer = VideoSerializer(video, data=request.data)

            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)

        except Exception as e:
            return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)