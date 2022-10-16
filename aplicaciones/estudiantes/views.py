from django.shortcuts import render,redirect
from .models import estudiante,grupo



#VISTAS DEL MENÚ
def index(request):
    return render(request,"index.html")

def contactanos(request):
    return render(request,"contactanos.html")

def nosotros(request):
    return render(request,"nosotros.html")

def demofree(request):
    return render(request,"demofree.html")
#FIN DE LAS VISTAS DEL MENÚ

#CRUD ESTUDIANTES
#CREAR
def registrarEstudiante(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    grupo = request.POST['grupo']

    estudiantee = estudiante.objects.create(nombre=nombre, apellido=apellido,id=grupo)
    return redirect('/')


    
#LISTAR 
def estudiantes(request):
    estudianteLista = estudiante.objects.all()
    grupoLista = grupo.objects.all()
    return render(request,"estudiantes.html",{"estudiantes": estudianteLista,"grupos":grupoLista})

