from django.db import models
from .models import Video
from reactions.models import Reaction
from comments.models import Comment

class ReactionCustomManager():
    def GetLikes(pk):
        like = Reaction.objects.filter(reaction_video=pk, reactions=Reaction.LIKE).count()
        return like

    def GetDISLikes(pk):
        dislike = Reaction.objects.filter(reaction_video=pk, reactions=Reaction.DISLIKE).count()
        return dislike

    def GetComments(pk):
        comment = Comment.objects.filter(video=pk).count()
        return comment
    def GetCommentList(pk):
        return Comment.objects.filter(Video=pk).order_by('-created_at')