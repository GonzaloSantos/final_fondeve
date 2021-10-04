from django . urls import path
from . views import index, contacto, postula,registrate


urlpatterns = [

    path('index/', index, name= "index"),
    path('contacto/',contacto, name= "contacto"),
    path('postula/' ,postula, name= "postula"),
    path('registrate/' ,registrate, name= "registrate"),
    
]