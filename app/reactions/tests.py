from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from videos.models import Video
from .models import Reaction
import pdb

# Create your tests here.
class ReactionAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='sam@gmail.com',
            password='password123'
        )
        self.client.login(email='sam@gmail.com', password='password123')

        self.reaction_video = Video.objects.create(
            title='test video',
            link='http://test.com',
            user=self.user
        )
    def test_reaction_detail_post(self):
        url = reverse('video-reaction', kwargs={'pk':self.reaction_video.id})

        data = {
            'reactions': Reaction.LIKE
        }

        res = self.client.post(url, data)
        print('로그 ==== ', Reaction.objects.get().reaction)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reaction.objects.count(), 1)
        self.assertEqual(Reaction.objects.get().reactions, Reaction.LIKE)

    def  test_reaction_detail_delete(self):
        pass
