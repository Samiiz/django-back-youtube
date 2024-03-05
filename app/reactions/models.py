from django.db import models
from django.db.models import Count,  Q
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Reaction(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction_video = models.ForeignKey(Video, on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction'),
    )

    reactions = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )

    @staticmethod
    def get_video_reaction(video):
        reactions = Reaction.objects.filter(reaction_video=video).aggregate(
            likes_count = Count('pk', filter=Q(reactions=Reaction.LIKE)),
            dislikes_count = Count('pk', filter=Q(reactions=Reaction.DISLIKE))
        )
        return reactions
