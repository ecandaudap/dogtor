from django.shortcuts import render
from rest_framework import viewsets, generics

# Models
from vet.models import PetOwner, Pet, PetDate

# Serializers
from .serializers import OwnersListSerializer, OwnersDetailSerializer,  PetListSerializer, PetDetailSerializer, PetDateListSerializer, PetDateDetailSerializer

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

# Pets

class ListPetsAPIView(generics.ListAPIView):
    """List Owners Api View"""

    queryset = Pet.objects.all().order_by("created_at")
   
    # serializadores
    serializer_class = PetListSerializer

class RetrievePetsAPIView(generics.RetrieveAPIView):
    """Detail Pet Owners Api View"""

    queryset = Pet.objects.all()
    serializer_class = PetDetailSerializer

class CreatePetsAPIView(generics.CreateAPIView):
    """Create new Pet Api View"""

    queryset = Pet.objects.all()
    serializer_class = PetDetailSerializer

class UpdatePetsAPIView(generics.UpdateAPIView):
    """Update Pet Api View"""

    queryset = Pet.objects.all()
    serializer_class = PetDetailSerializer

class DestroyPetsAPIView(generics.DestroyAPIView):
    """Delete Pet Owners Api View"""

    queryset = Pet.objects.all()
    serializer_class = PetDetailSerializer

# Pet  Dates

class ListPetDatesAPIView(generics.ListAPIView):
    """List Owners Api View"""

    queryset = PetDate.objects.all().order_by("created_at")
   
    # serializadores
    serializer_class = PetDateListSerializer

class RetrievePetDatesAPIView(generics.RetrieveAPIView):
    """Detail PetDate Owners Api View"""

    queryset = PetDate.objects.all()
    serializer_class = PetDateDetailSerializer

class CreatePetDatesAPIView(generics.CreateAPIView):
    """Create new PetDate Api View"""

    queryset = PetDate.objects.all()
    serializer_class = PetDateDetailSerializer

class UpdatePetDatesAPIView(generics.UpdateAPIView):
    """Update PetDate Api View"""

    queryset = PetDate.objects.all()
    serializer_class = PetDateDetailSerializer

class DestroyPetDatesAPIView(generics.DestroyAPIView):
    """Delete PetDate Owners Api View"""

    queryset = PetDate.objects.all()
    serializer_class = PetDateDetailSerializer