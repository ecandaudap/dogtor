from django.contrib import admin

# Register your models here.

# Models
from .import models

# Panel de administración para la app de 'blog'
class VetAdminArea(admin.AdminSite):
    '''Blog admin panel administration'''

    site_header = "Vet Site Admin Area"


# Instanciar nuestra clase para poder utilizar
vet_admin_site = VetAdminArea(name="VetAdmin")

# Registramos modelo 'Post' en nuestro admin.area
vet_admin_site.register(models.PetOwner)
vet_admin_site.register(models.Pet)
vet_admin_site.register(models.PetDate)

# Registrarlo en el admin area general de admin
admin.site.register(models.PetOwner)
admin.site.register(models.Pet)
admin.site.register(models.PetDate)

