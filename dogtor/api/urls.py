from django.urls import path, include
from rest_framework import routers


# Views
from .views import OwnerViewSet, PetViewSet, PetDateViewSet

# Router
router = routers. DefaultRouter()
router.register(r"owners", OwnerViewSet)
router.register(r"pets", PetViewSet)
router.register(r"petdates", PetDateViewSet)


urlpatterns = [path("", include(router.urls))]


