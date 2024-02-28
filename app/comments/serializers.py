from rest_framework.serializers import ModelSerializer
from .models import Comment
from users.serializers import UserSerializer

class CommentSerializer(ModelSerializer):
    # UserSerializer를 불러와서 user로 정의함
    user = UserSerializer()
    class Meta:
        model = Comment
        # Comment에 대한 표기할 내용
        fields = ('user', 'like', 'dislike', 'content',)