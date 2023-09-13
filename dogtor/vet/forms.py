from django import forms


#Importamos los modelos
from .models import PetOwner, Pet


# Los formularios se tienen que vincular con los modelos.

# Los formularios -> CLASES

class OwnerForm(forms.ModelForm):



    class Meta:
        model = PetOwner
        fields = ("first_name", "last_name", "address", "email", "phone")


class PetForm(forms.ModelForm):



    class Meta:
        model = Pet
        fields = ("name", "type", "owner")