from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from videos.models import Video

import pdb

class VideoAPITestCase(APITestCase):
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
    def test_video_list_get(self):
        url = reverse('video-list')
        print('url', url) # 이거는 /api/v1/videos/

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_video_detail_get(self):
        # url확인 reverse(urlpattern)
        url = reverse('video-detail', kwargs={"pk":self.video.pk})
        print('url', url) # 이거는 /api/v1/videos/1/
        # url,(kwargs)요청 res = self.client.get(url, kwargs)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_video_list_post(self):
        url = reverse('video-list')
        print(f"'user': {self.user.pk}")
        data = {
            'title': 'test video',
            'link': 'http://test.com',
            'category': 'test_category',
            'thumbnail': 'http://test.com',
            'video_uploaded_url': "http://test.com",
            'video_file': SimpleUploadedFile('file.mp4',b"file_content", content_type='video/mp4'),
            'user': self.user.pk
        }

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_video_detail_put(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})

        data = {
            'title': 'update video',
            'link': 'http://update.com',
            'category': 'test_category',
            'thumbnail': 'http://update.com',
            'video_uploaded_url': "http://test.com",
            'video_file': SimpleUploadedFile('file.mp4',b"file_content", content_type='video/mp4'),
            'user': self.user.pk
        }

        res = self.client.put(url,data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], 'update video')

    def test_video_detail_delete(self):
        url=reverse('video-detail', kwargs={'pk':self.video.pk})
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)