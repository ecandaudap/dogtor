from django.shortcuts import render
from rest_framework import viewsets, generics

# Models
from vet.models import PetOwner, Pet, PetDate

# Serializers
from .serializers import OwnersListSerializer, OwnersDetailSerializer

# Create your views here.


# LIST -> GET
# RETRIEVE -> GET
# class OwnerViewSet(viewsets.ModelViewSet):
#     """Viewset del modelo PetOwner"""

#     #1 queryset que se va realizar -> ORM
#     #2 El serializador

#     queryset = PetOwner.objects.all()
#     serializer_class = OwnerSerializer

# class PetViewSet(viewsets.ModelViewSet):
    # """Viewset del modelo Pet"""
# 
    # queryset = Pet.objects.all()
    # serializer_class = PetSerializer
# 
# class PetDateViewSet(viewsets.ModelViewSet):
    # """Viewset del modelo PetDate"""
# 
    # queryset = PetDate.objects.all()
    # serializer_class = PetDateSerializer

class ListOwnersAPIView(generics.ListAPIView):
    """List Owners Api View"""

    queryset = PetOwner.objects.all().order_by("created_at")
   
    # serializadores
    serializer_class = OwnersListSerializer

class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    """Detail Pet Owners Api View"""

    queryset = PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer

class CreateOwnersAPIView(generics.CreateAPIView):
    """Create new Pet Owners Api View"""

    queryset = PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer

class UpdateOwnersAPIView(generics.UpdateAPIView):
    """Update Pet Owners Api View"""

    queryset = PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer

class DestroyOwnersAPIView(generics.DestroyAPIView):
    """Delete Pet Owners Api View"""

    queryset = PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer