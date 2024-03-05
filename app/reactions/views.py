from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from  videos.models import Video
from .models import Reaction
from .serializers import ReactionSerializer

# Create your views here.
class ReactionDetail(APIView):
    # reaction, created = Reaction.objects.get_or_create(user_data) <- 이걸로 인해서 get_object함수 필요 없어짐!
    # def get_object(self, pk):
    #     # return get_object_or_404(Video, pk=pk)
    #     try:
    #         return Video.objects.get(pk=pk)
    #     except Video.DoesNotExist:
    #         raise NotFound
    def post(self, request, pk):

        user_data = request.data
        serilaizer = ReactionSerializer(data=user_data)

        if serilaizer.is_valid():
            reaction_obj, created = Reaction.objects.get_or_create(
                user=request.user,
                reaction_video=Video.objects.get(pk=pk),
                defaults={
                    'reactions': serilaizer.validated_data['reactions']
                }
            )
            if created:
                return Response(serilaizer.data, status=status.HTTP_201_CREATED)
            if not created:
                reaction_obj.reactions = serilaizer.validated_data['reactions']
                reaction_obj.save()
                return Response(serilaizer.data, status=status.HTTP_200_OK)