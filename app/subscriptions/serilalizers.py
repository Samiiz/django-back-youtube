from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Subscription
from users.serializers import UserSerializer as sub
from users.serializers import UserSerializer as sub_to

class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
    def validate(self, data):
        if data['subscriber'] == data['subscribed_to']:
            raise serializers.ValidationError('Subscriber and subscribed_to cannot be the same')
        return data

# 내가 만든 거
# class SubcriptionSerializer(ModelSerializer):
#     user1 = sub(read_only=True)
#     user2 = sub_to(read_only=True)

#     class Meta:
#         model = Subcription
#         fields = '__all__'