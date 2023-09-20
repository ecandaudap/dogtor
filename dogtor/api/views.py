from django.shortcuts import render
from rest_framework import viewsets

# Models
from vet.models import PetOwner, Pet, PetDate

# Serializers
from .serializers import OwnerSerializer, PetSerializer, PetDateSerializer

# Create your views here.


# LIST -> GET
# RETRIEVE -> GET
class OwnerViewSet(viewsets.ModelViewSet):
    """Viewset del modelo PetOwner"""

    #1 queryset que se va realizar -> ORM
    #2 El serializador

    queryset = PetOwner.objects.all()
    serializer_class = OwnerSerializer

class PetViewSet(viewsets.ModelViewSet):
    """Viewset del modelo Pet"""

    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetDateViewSet(viewsets.ModelViewSet):
    """Viewset del modelo PetDate"""

    queryset = PetDate.objects.all()
    serializer_class = PetDateSerializer