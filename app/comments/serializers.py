from rest_framework.serializers import ModelSerializer
from .models import Comment
from users.serializers import UserSerializer

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        # Comment에 대한 표기할 내용
        fields = '__all__'
        read_only_fields = ('user', 'Video')