from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from cards.models import Card


class CardTest(APITestCase):
    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.card = Card.objects.create(name='New Card',
                                        description='Card description',
                                        creation_date='2021-7-13 11:30:00',
                                        limit_date='2021-7-15 12:00:00',
                                        position='1')
        User.objects.create_user(username='user', password='password', is_staff=True)
        response = self.client.post(f'{self.host}/api/token/', data={'username': 'user', 'password': 'password'})
        assert response.status_code == 200, response.status_code
        self.token = response.data['access']

    def test_get_board(self):
        response = self.client.get(f'{self.host}/cards/')
        self.assertNotEqual(len(response.data), 0)

    def test_create_card(self):
        response = self.client.post(f'{self.host}/cards/',
                                   data={'name': 'New Card',
                                         'description': 'Card description',
                                         'creation_date': '2021-7-13 11:30:00',
                                         'limit_date': '2021-7-15 12:00:00',
                                         'position': '1'},
                                   HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 201)
        total_cards = Card.objects.all().count()
        self.assertNotEqual(total_cards, 0)

    def test_update_card(self):
        response = self.client.patch(f'{self.host}/cards/{self.card.id}/',
                                     data={'name':'Project Leader', 'description':'Tasks'},
                                     HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 200)

    def test_delete_card(self):
        response = self.client.delete(f'{self.host}/cards/{self.card.id}/', HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 204)
        total_cards = Card.objects.all().count()
        self.assertEqual(total_cards, 0)