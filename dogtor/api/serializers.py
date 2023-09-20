from rest_framework import serializers

# Modelos
from vet.models import PetOwner

class OwnerSerializers(serializers.HyperlinkedModelSerializer):
    """Pet owners serializer"""

    class Meta:
        model = PetOwner
        fields = ["id",
                  "first_name",
                  "last_name",
                  "email",
                  "address",
                  "phone",
                  "created_at",
                  ]