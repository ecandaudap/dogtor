from django.shortcuts import render
from rest_framework import viewsets

# Models
from vet.models import PetOwner

# Serializers
from .serializers import OwnerSerializers

# Create your views here.


# LIST -> GET
# RETRIEVE -> GET
class OwnerViewSet(viewsets.ModelViewSet):
    """Viewset del modelo PetOwner"""

    #1 queryset que se va realizar -> ORM
    #2 El serializador

    queryset = PetOwner.objects.all()
    serializer_class = OwnerSerializers