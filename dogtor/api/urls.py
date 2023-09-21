from django.urls import path, include
from rest_framework import routers


# Views
from .views import ListOwnersAPIView, RetrieveOwnersAPIView, CreateOwnersAPIView, UpdateOwnersAPIView, DestroyOwnersAPIView

# Router
# router = routers. DefaultRouter()
# router.register(r"owners", OwnerViewSet)
# router.register(r"pets", PetViewSet)
# router.register(r"petdates", PetDateViewSet)


urlpatterns = [
    #path("", include(router.urls))
    path("owners/", ListOwnersAPIView.as_view(), name="owners_list"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="owners_detail"),
    path("owners/add/", CreateOwnersAPIView.as_view(), name="owners_create"),
    path("owners/<int:pk>/update/", UpdateOwnersAPIView.as_view(), name="owners_update"),
    path("owners/<int:pk>/destroy/", DestroyOwnersAPIView.as_view(), name="owners_delete"),
    ]


