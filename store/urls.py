from django.urls import path, include
from rest_framework import routers

from store.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='Orders')

urlpatterns = [
    path('api/', include(router.urls))
]
