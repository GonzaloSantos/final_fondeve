from django.shortcuts import render
from .forms import ContactoForm,JuntaForm,RepresentanteForm, ImageForm
from django .contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *



# Create your views here.
def index(request):
    return render (request,'app/index.html')

def contacto (request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["Mensaje"] = "Mensaje enviado"
        else:
            data["form"]= formulario

    return render(request,'app/contacto.html',data)

def postula (request):

    data={
        'form':RepresentanteForm()
    }

    if request.method =='POST':
        formulario = RepresentanteForm(data=request.POST)
        imagen= request.FILES.get('txtimagen')
        if formulario.is_valid():
            formulario.save()
            data["Mensaje"] = "Mensaje enviado"
        else:
            data["form"]= formulario
    return render (request,'app/postula.html',data)

def registrate (request):
    data={
        'form':JuntaForm(),
        'formulario_imagen':ImageForm()
    }
    if request.method =='POST':
        formulario = JuntaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            img_obj = formulario.instance
            data["Mensaje"] = "Mensaje enviado"
            return render (request,'app/registrate.html', {'formulario': formulario, 'img_obj': img_obj})

        else:
            data["form"]= formulario
    return render (request,'app/registrate.html', data)

'''
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
'''