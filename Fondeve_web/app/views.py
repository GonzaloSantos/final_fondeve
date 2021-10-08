from django.shortcuts import render
from .forms import ContactoForm,JuntaForm,RepresentanteForm, ImageForm
from django .contrib import messages




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
def registrate (request):
    data={
        'form':JuntaForm()
    }
    if request.method =='POST':
        formulario = JuntaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["Mensaje"] = "Mensaje enviado"
        else:
            data["form"]= formulario
    return render (request,'app/registrate.html',data)

'''
