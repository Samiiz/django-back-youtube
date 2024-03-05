from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer
from reactions.models import Reaction
# from reactions.serializers import ReactionSerializer


class VideoSerializer(ModelSerializer):
    # UserSerializer를 불러와서 user로 정의함
    user = UserSerializer(read_only=True)
    # comments는 video에 대하여 1:n 관계 임으로 comment'_set'으로 역참조 가능하도록 만들어준다.
    comment_set = CommentSerializer(many=True, read_only=True)
    # reaction_set = ReactionSerializer(many=True, read_only=True)

    reactions = serializers.SerializerMethodField()

    LikesCount = serializers.IntegerField(read_only=True)
    DisLIkesCount = serializers.IntegerField(read_only=True)
    class Meta:
        model = Video
        fields = '__all__'

    def get_reactions(self, video):
        return Reaction.get_video_reaction(video)