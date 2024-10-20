from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class AuthenticationTest(APITestCase):

    def test_user_registration(self):
        """Test user registration"""
        url = reverse('user-list')  # Имя маршрута для регистрации пользователя
        data = {
            'username': 'testuser',
            'password': 'A3StrongPassword@2024',  # Используем более сложный пароль
            'email': 'testuser@example.com'
        }
        response = self.client.post(url, data)

        # Выводим ответ для анализа (если нужно)
        print(response.data)  # Это можно убрать после успешного теста

        # Ожидаемый статус 201 (создан)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_token_login(self):
        """Test obtaining authentication token"""
        # Создадим пользователя
        user = User.objects.create_user(username='testuser', password='password123')

        url = reverse('login')  # Djoser автоматически создает этот маршрут
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.data)

    def test_token_logout(self):
        """Test logging out (deleting the token)"""
        # Создадим пользователя и получим токен
        user = User.objects.create_user(username='testuser', password='password123')
        login_url = reverse('login')
        login_data = {
            'username': 'testuser',
            'password': 'password123'
        }
        login_response = self.client.post(login_url, login_data)
        token = login_response.data['auth_token']

        # Проверим выход из системы
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        logout_url = reverse('logout')
        logout_response = self.client.post(logout_url)
        self.assertEqual(logout_response.status_code, status.HTTP_204_NO_CONTENT)
