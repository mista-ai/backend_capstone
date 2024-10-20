from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pizza", price=10.99, inventory=20)
        self.menu2 = Menu.objects.create(title="Burger", price=8.99, inventory=15)

    def test_get_all_menu_items(self):
        """Test getting all menu items"""
        response = self.client.get(reverse('menu'))
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_menu_item(self):
        """Test getting a single menu item"""
        url = reverse('single-menu-item', args=[self.menu1.id])
        response = self.client.get(url)
        serializer = MenuSerializer(self.menu1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_menu_item(self):
        """Test creating a new menu item"""
        payload = {
            "title": "Salad",
            "price": 5.99,
            "inventory": 30
        }
        response = self.client.post(reverse('menu'), payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.booking1 = Booking.objects.create(name="John Doe", number_of_guests=2, booking_date="2024-10-20 18:00:00")
        self.booking2 = Booking.objects.create(name="Jane Doe", number_of_guests=4, booking_date="2024-10-21 19:00:00")

    def test_get_all_bookings(self):
        """Test getting all bookings"""
        response = self.client.get(reverse('tables-list'))  # Имя маршрута должно быть 'tables-list'
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_booking(self):
        """Test creating a new booking"""
        payload = {
            "name": "Alice",
            "number_of_guests": 3,
            "booking_date": "2024-10-22 20:00:00"
        }
        response = self.client.post(reverse('tables-list'), payload)  # Имя маршрута должно быть 'tables-list'
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
