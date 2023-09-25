from django.urls import path, include
from rest_framework import routers


# Views
from .views import ListOwnersAPIView, RetrieveOwnersAPIView, CreateOwnersAPIView, UpdateOwnersAPIView, DestroyOwnersAPIView,  ListPetsAPIView, RetrievePetsAPIView, CreatePetsAPIView, UpdatePetsAPIView, DestroyPetsAPIView, ListPetDatesAPIView, RetrievePetDatesAPIView, CreatePetDatesAPIView, UpdatePetDatesAPIView, DestroyPetDatesAPIView

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
    path("pets/", ListPetsAPIView.as_view(), name="pets_list"),
    path("pets/<int:pk>/", RetrievePetsAPIView.as_view(), name="pets_detail"),
    path("pets/add/", CreatePetsAPIView.as_view(), name="pets_create"),
    path("pets/<int:pk>/update/", UpdatePetsAPIView.as_view(), name="pets_update"),
    path("pets/<int:pk>/destroy/", DestroyPetsAPIView.as_view(), name="pets_delete"),
    path("petdates/", ListPetDatesAPIView.as_view(), name="petdates_list"),
    path("petdates/<int:pk>/", RetrievePetDatesAPIView.as_view(), name="petdates_detail"),
    path("petdates/add/", CreatePetDatesAPIView.as_view(), name="petdates_create"),
    path("petdates/<int:pk>/update/", UpdatePetDatesAPIView.as_view(), name="petdates_update"),
    path("petdates/<int:pk>/destroy/", DestroyPetDatesAPIView.as_view(), name="petdates_delete"),
    ]


