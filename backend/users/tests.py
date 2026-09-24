from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AuthTests(APITestCase):
    def test_register_user_with_default_role(self):
        """Teste l'inscription d'un nouvel utilisateur avec le rôle par défaut."""
        url = reverse('register')
        response = self.client.post(url, {
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'password12345'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_with_short_password(self):
        """Teste l'inscription d'un nouvel utilisateur avec un mot de passe trop court."""
        url = reverse('register')
        response = self.client.post(url, {
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'short'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_returns_tokens(self):
        """Teste que la connexion retourne les tokens d'accès et de rafraîchissement."""
        user = User.objects.create_user(username='charlie', email='charlie@example.com', password='password12345')
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'charlie',
            'password': 'password12345'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_me_requires_authentication(self):
        """Teste que l'accès à l'endpoint 'me' nécessite une authentification."""
        url = reverse('me')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_me_returns_user_profile(self):
        """Teste que l'endpoint 'me' retourne les informations de l'utilisateur connecté."""
        user = User.objects.create_user(username='dave', email='dave@example.com', password='password12345')
        token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
        url = reverse('me')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'dave')
        self.assertEqual(response.data['role'], 'USER')