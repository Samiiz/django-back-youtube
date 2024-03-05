from django.db import models
from users.models import User
from common.models import CommonModel
# Create your models here.

class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, through='ChatRoomMember')

class ChatRoomMember(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ChatMessage(CommonModel):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()