from django.urls import path, include
from rest_framework import routers


# Views
from .views import OwnerViewSet

# Router
router = routers. DefaultRouter()
router.register(r"owners", OwnerViewSet)


urlpatterns = [path("", include(router.urls))]


