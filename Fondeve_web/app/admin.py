from django.contrib import admin
from .models import Contacto,Junta,Representante

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display =["nombre","correo","tipo_consulta","mensaje"]
    search_fields=["nombre"]


class JuntaAdmin(admin.ModelAdmin):
    list_display =["nombre","rut","direccion","imagen"]
    search_fields=["nombre"]

class RepresentanteAdmin(admin.ModelAdmin):
    list_display =["nombre","rut","telefono","email"]
    search_fields=["nombre"]

admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Junta,JuntaAdmin)
admin.site.register(Representante,RepresentanteAdmin)

