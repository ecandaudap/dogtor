from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Models
from vet.models import PetOwner, Pet

# Forms
from .forms import OwnerForm, PetForm

# Create your views here.
def list_pet_owners(request):
    '''List owners'''
    
    # Agarrar información de la BD
    owners = PetOwner.objects.all()

    # Hacemos el contexto
    context = {"owners": owners}

    # Agarrar template
    template = loader.get_template("vet/owners/list.html")

    # Retornar respuesta HTTP con el template pasandole el contexto
    return HttpResponse(template.render(context, request))


# class OwnersList(TemplateView):
#     # Renderiza este Template
#     template_name = "vet/owners/list.html"

#     # Este template va a tener cierto contexto
#     def get_context_data(self, **kwargs):
#         # Agarrar el contexto que ya creo 'TemplateView'
#         context = super().get_context_data(**kwargs)
#         # Le agregamos nuestro custom context
#         context["owners"] = PetOwner.objects.all()

#         return context


class OwnersList(ListView):
    '''Render all pet owner'''

    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"

class OwnerDetail(DetailView):
    '''Render a specific Pet Owner with their pk'''

    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"

class OwnersCreate(CreateView):
    '''View used to create a PetOwner'''

    # 1. Modelo
    # 2. Template a renderizar
    # 3. El formulario con el que se va a crear 
    # 4  La url a direccionar si la request fue exitosa -> reversed_url

    model = PetOwner #1
    template_name = "vet/owners/create.html" #2
    form_class = OwnerForm #3

    # url a donde se va redireccionar si fue exitosa nuestra creación
    success_url = reverse_lazy("vet:owners_list")

class OwnersUpdate(UpdateView):
    '''View used to update Petowner'''

    model = PetOwner
    template_name = "vet/owners/update.html"
    form_class = OwnerForm

    success_url = reverse_lazy("vet:owners_list")

class Test(View):
    # Cada vista va a tener como función el método (GET, PATCH, POST, DELETE, PUT)
    def get(self, request):    
        return HttpResponse("Hello world from a classic generic review")


# class PetsList(TemplateView):
#     # Renderiza este Template
#     template_name = "vet/pets/list.html"

#     # Este template va a tener cierto contexto
#     def get_context_data(self, **kwargs):
#         # Agarrar el contexto que ya creo 'TemplateView'
#         context = super().get_context_data(**kwargs)
#         # Le agregamos nuestro custom context
#         context["pets"] = Pet.objects.all()

#         return context

# class PetsDetail(TemplateView):
#     # Renderiza este Template
#     template_name = "vet/pets/detail.html"

#     # Este template va a tener cierto contexto
#     def get_context_data(self, **kwargs):
#         # Agarrar el contexto que ya creo 'TemplateView'
#         context = super().get_context_data(**kwargs)
#         # Le agregamos nuestro custom context
#         context["pet"] = Pet.objects.get(pk=kwargs["pk"])

#         return context

class PetsList(ListView):
    '''Render all pet list'''

    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"

class PetsDetail(DetailView):
    '''Render a specific Pet with their pk'''

    model = Pet
    template_name = "vet/pets/details.html"
    context_object_name = "pets"

class PetsCreate(CreateView):
    '''View used to create a Pet'''

    model = Pet
    template_name = "vet/pets/create.html"
    form_class = PetForm

    # url a donde se va redireccionar si fue exitosa nuestra creación
    success_url = reverse_lazy("vet:pets_list")

class PetsUpdate(UpdateView):
    '''View used to update Petowner'''

    model = Pet
    template_name = "vet/pets/update.html"
    form_class = PetForm

    success_url = reverse_lazy("vet:pets_list")
