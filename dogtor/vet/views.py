from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView

# Models
from vet.models import PetOwner

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


class OwnersList(TemplateView):
    # Renderiza este Template
    template_name = "vet/owners/list.html"

    # Este template va a tener cierto contexto
    def get_context_data(self, **kwargs):
        # Agarrar el contexto que ya creo 'TemplateView'
        context = super().get_context_data(**kwargs)
        # Le agregamos nuestro custom context
        context["owners"] = PetOwner.objects.all()

        return context


class Test(View):
    # Cada vista va a tener como función el método (GET, PATCH, POST, DELETE, PUT)
    def get(self, request):    
        return HttpResponse("Hello world from a classic generic review")




