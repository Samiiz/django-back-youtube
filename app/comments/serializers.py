from rest_framework.serializers import ModelSerializer
from .models import Comment
from users.serializers import UserSerializer

class CommentSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('user', 'like', 'dislike', 'content',)