from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80.00")


class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(title="Pizza", price=10.99, inventory=20)

    def test_menu_str(self):
        """Test string representation of Menu model"""
        self.assertEqual(str(self.menu_item), "Pizza : 10.99")

    def test_menu_inventory(self):
        """Test inventory field"""
        self.assertEqual(self.menu_item.inventory, 20)


class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(name="John Doe", number_of_guests=4, booking_date="2024-10-20 19:00")

    def test_booking_str(self):
        """Test string representation of Booking model"""
        self.assertEqual(str(self.booking), "John Doe")

    def test_booking_guests(self):
        """Test number_of_guests field"""
        self.assertEqual(self.booking.number_of_guests, 4)
