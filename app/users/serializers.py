from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # user에 대한 표기할 내용
        fields = ('id', 'nickname', 'email',)