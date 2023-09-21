from rest_framework import serializers

# Modelos
from vet.models import PetOwner, Pet, PetDate

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    """Pet owners serializer"""

    class Meta:
        model = PetOwner
        fields = [
            "id", 
            "first_name",
            "last_name",
            "email",
            "address",
            "phone",
            "created_at",
                  ]

class PetSerializer(serializers.HyperlinkedModelSerializer):
    """Pet serializer"""

    # PrimaryKeyRelatedField
    owner = serializers.PrimaryKeyRelatedField(queryset=PetOwner.objects.all(),
                                                  many=False)

    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "type",
            "created_at",
            "owner",
                  ]

class PetDateSerializer(serializers.HyperlinkedModelSerializer):
    """Pet date serializer"""

    # PrimaryKeyRelatedField
    pet = serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all(),
                                                  many=False)

    class Meta:
        model = PetDate
        fields = [
            "id",
            "datetime",
            "type",
            "created_at",
            "pet",
                  ]

class OwnersListSerializer(serializers.ModelSerializer):
    """serializer to list all Pet Owners"""

    class Meta:
        model = PetOwner
        fields =["first_name", "last_name"]

class OwnersDetailSerializer(serializers.ModelSerializer):
    """serializer to detail Pet Owners"""

    class Meta:
        model = PetOwner
        fields ="_all_"

class OwnerCreateSerializer(serializers.ModelSerializer):
    """serializer to create Pet Owners"""

    class Meta:
        model = PetOwner
        fields ="__all__"

class OwnerUpdateSerializer(serializers.ModelSerializer):
    """serializer to update Pet Owners"""

    class Meta:
        model = PetOwner
        fields ="__all__"

class OwnerDestroySerializer(serializers.ModelSerializer):
    """serializer to delete Pet Owners"""

    class Meta:
        model = PetOwner
        fields ="__all__"