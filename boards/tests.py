from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from boards.models import Board


class BoardTestCase(APITestCase):

    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.board = Board.objects.create(name='New Board',
                                          description='New Project',
                                          creation_date='2021-7-13 11:30:00',
                                          visibility=True)
        User.objects.create_user(username='user', password='password', is_staff=True)
        response = self.client.post(f'{self.host}/api/token/', data={'username': 'user', 'password': 'password'})
        assert response.status_code == 200, response.status_code
        self.token = response.data['access']

    def test_get_board(self):
        response = self.client.get('https://127.0.0.1:8000/boards/')
        self.assertNotEqual(len(response.data), 0)

    def test_create_board(self):
        response = self.client.post(f'{self.host}/boards/',
                                    data={'name': 'New Board', 'description': 'New Project',
                                          'creation_date': '2021-7-13 11:30:00', 'visibility':'True'},
                                    HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 201)
        total_boards = Board.objects.all().count()
        self.assertNotEqual(total_boards, 0)

    def test_update_board(self):
        response = self.client.patch(f'{self.host}/boards/{self.board.id}/',
                                     data={'name': 'Django API', 'description': 'TaskMaster'},
                                     HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 200)

    def test_delete_board(self):
        response = self.client.delete(f'{self.host}/boards/{self.board.id}/', HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 204)
        total_boards = Board.objects.all().count()
        self.assertEqual(total_boards, 0)