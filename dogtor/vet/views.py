from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

# Models
from vet.models import PetOwner, Pet

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

class Test(View):
    # Cada vista va a tener como función el método (GET, PATCH, POST, DELETE, PUT)
    def get(self, request):    
        return HttpResponse("Hello world from a classic generic review")


class PetsList(TemplateView):
    # Renderiza este Template
    template_name = "vet/pets/list.html"

    # Este template va a tener cierto contexto
    def get_context_data(self, **kwargs):
        # Agarrar el contexto que ya creo 'TemplateView'
        context = super().get_context_data(**kwargs)
        # Le agregamos nuestro custom context
        context["pets"] = Pet.objects.all()

        return context

class PetsDetail(TemplateView):
    # Renderiza este Template
    template_name = "vet/pets/detail.html"

    # Este template va a tener cierto contexto
    def get_context_data(self, **kwargs):
        # Agarrar el contexto que ya creo 'TemplateView'
        context = super().get_context_data(**kwargs)
        # Le agregamos nuestro custom context
        context["pet"] = Pet.objects.get(pk=kwargs["pk"])

        return context