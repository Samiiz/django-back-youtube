from rest_framework.serializers import ModelSerializer
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer


class VideoSerializer(ModelSerializer):
    user = UserSerializer()
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Video
        fields = '__all__'