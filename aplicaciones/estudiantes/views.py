from django.shortcuts import render
from .models import estudiante,grupo

# Create your views here.
def inicio(request):
    estudianteLista = estudiante.objects.all()
    return render(request,"listarEstudiantes.html",{"estudiantes": estudianteLista})
   # return HttpResponse("<h1>hola mundo!</h1>")