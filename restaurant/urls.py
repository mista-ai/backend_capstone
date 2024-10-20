from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'tables', views.BookingViewSet, basename='tables')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('restaurant/booking/', include(router.urls)),
]
