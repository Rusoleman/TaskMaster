from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from lists.models import List


class ListTest(APITestCase):
    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.list = List.objects.create(name='New list', creation_date='2021-7-13 11:30:00', position=1)
        User.objects.create_user(username='user', password='password', is_staff=True)
        response = self.client.post(f'{self.host}/api/token/', data={'username': 'user', 'password': 'password'})
        assert response.status_code == 200, response.status_code
        self.token = response.data['access']

    def test_get_list(self):
        response = self.client.get(f'{self.host}/lists/')
        self.assertNotEqual(len(response.data), 0)

    def test_create_list(self):
        response = self.client.post(f'{self.host}/lists/',
                                    data={'name': 'New list',
                                          'creation_date':'2021-7-13 11:30:00',
                                          'position':'1'},
                                    HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 201)
        total_lists = List.objects.all().count()
        self.assertNotEqual(total_lists, 0)

    def test_update_list(self):
        response = self.client.patch(f'{self.host}/lists/{self.list.id}/',
                                     data={'name': 'My list'},
                                     HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 200)

    def test_update_list(self):
        response = self.client.delete(f'{self.host}/lists/{self.list.id}/', HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 204)
        total_lists = List.objects.all().count()
        self.assertEqual(total_lists, 0)