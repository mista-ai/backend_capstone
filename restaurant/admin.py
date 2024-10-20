from django.contrib import admin
from .models import Booking, Menu


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number_of_guests', 'booking_date')
    # list_editable = ('number_of_guests', 'booking_date')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'inventory')
    # list_editable = ('title', 'price', 'inventory')
