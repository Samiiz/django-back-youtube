from django.db import models
from django.db.models import Count,  Q, Manager
from common.models import CommonModel
from users.models import User

# class ViedeoManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().annotate(
#             # LikesCount=models.Count('model', filter=models.Q(model__field=값))
#             LikesCount=models.Count('reaction', filter=models.Q(reaction__reactions=1)),
#             DisLIkesCount=models.Count('reaction', filter=models.Q(reaction__reactions=-1))
#         )

# Create your models here.
class Video(CommonModel):
    title = models.CharField(max_length=255)
    link = models.URLField()
    desription = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField()
    video_uploaded_url = models.URLField()
    video_file = models.FileField(upload_to='storage/')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # objects = ViedeoManager()