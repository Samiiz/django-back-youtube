from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User

# Create your tests here.
class Test_Create_ChatRoom(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email='sam@gmail.com',
            password='password123'
        )
        self.user2 = User.objects.create_user(
            email='sam2@gmail.com',
            password='password123'
        )
        self.client.login(email='sam@gmail.com', password='password123')
    
    def test_create_chat_room(self):
        url = reverse('room-list')
        data = {
            "name": "testromm1",
        }
        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)