from django.db import models

# Create your models here.
class Junta(models.Model):
    nombre=models.CharField(max_length=50)
    rut=models.IntegerField()
    direccion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Representante(models.Model):
    nombre=models.CharField(max_length=50)
    rut=models.IntegerField()
    telefono=models.IntegerField()
    email= models.EmailField (max_length=254)
    imagen= models.ImageField(upload_to="imagenes",null=True)

    def __str__(self):
        return self.nombre

opciones_consutlas =[
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]

]

class Contacto(models.Model):
    nombre= models. CharField(max_length=50)
    correo= models.EmailField()
    tipo_consulta=models.IntegerField(choices=opciones_consutlas)
    mensaje= models.TextField()

    def __str__(self):
        return self.nombre