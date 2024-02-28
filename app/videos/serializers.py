from rest_framework.serializers import ModelSerializer
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer


class VideoSerializer(ModelSerializer):
    # UserSerializer를 불러와서 user로 정의함
    user = UserSerializer()
    # comments는 video에 대하여 1:n 관계 임으로 comment'_set'으로 역참조 가능하도록 만들어준다.
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Video
        fields = '__all__'