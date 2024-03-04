from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from users.models import User
from .models import Subscription
from users.serializers import UserSerializer
from .serilalizers  import SubscriptionSerializer
import pdb
# Create your views here.

# 수업
class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data

        serializer = SubscriptionSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SubscriptionDetail(APIView):
    def delete(self, request, pk):
        subs = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        subs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 내가만든거
# class SubscriptionList(APIView):
#     def get_user(self, pk):
#         return get_object_or_404(User, pk=pk)
#     def post(self, request):
#         data = {
#             "subscriber": request.user.pk,
#             "subscribed_to": request.data['subscribed_to']
#         }
#         try:
#             serilaizer = SubcriptionSerializer(data=data)

#             if serilaizer.is_valid():
#                 serilaizer.save()
#                 return Response(serilaizer.data, status=status.HTTP_201_CREATED)
#             return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)

# class SubscriptionDetail(APIView):
#     def get_user(self, pk):
#         return get_object_or_404(User, pk=pk)
#     def delete(self, request, pk):
#         subs = Subcription.objects.filter(subscriber=request.user.pk, subscribed_to=pk)
#         print(subs)
#         subs.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)