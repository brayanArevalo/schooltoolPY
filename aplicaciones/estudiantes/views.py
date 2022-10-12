from django.shortcuts import render
from .models import estudiante,grupo

def listarEstudiantes(request):
    estudianteLista = estudiante.objects.all()
    return render(request,"listarEstudiantes.html",{"estudiantes": estudianteLista})

def index(request):
    return render(request,"index.html")

def contactanos(request):
    return render(request,"contactanos.html")

def nosotros(request):
    return render(request,"nosotros.html")



