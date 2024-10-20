from django.contrib import admin
from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register(r'auth/users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken'))
]
