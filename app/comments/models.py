from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video


class Comment(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Video = models.ForeignKey(Video, on_delete=models.CASCADE)

    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    content = models.TextField()