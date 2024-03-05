from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from videos.models import Video
import pdb

class CommentAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='sam@gmail.com',
            password='password123'
        )
        self.client.login(email='sam@gmail.com', password='password123')
        self.video = Video.objects.create(
            title='test video',
            link='http://test.com',
            user=self.user
        )
    def test_comment_create(self):
        url = reverse('video-comment', kwargs={'pk':self.video.pk})
        data = {
            'content': 'test comment',
        }

        res = self.client.post(url, data)
        pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_comment_list(self):
        url = reverse('video-comment', kwargs={'pk':self.video.pk})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_commen_count(self):
        url = reverse('video-comment', kwargs={'pk':self.video.pk})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)