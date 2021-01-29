from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet


router = DefaultRouter()
router.register('', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]