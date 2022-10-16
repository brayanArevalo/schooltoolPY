from . import views
from django.urls import path

urlpatterns =[
    path('',views.index,name='index'),
    path('contactanos/',views.contactanos,name='contactanos'),
    #path('/',views.index, name="index"),
    path('demofree/',views.demofree,name="demofree"),
    path('demofree/estudiantes/',views.estudiantes,name='estudiantes'),
    path('nosotros/',views.nosotros,name ='nosotros'),
    path('registrarEstudiante/', views.registrarEstudiante, name='registrarEstudiante'),
    #path('eliminarEstudiante/<id>',views.eliminarEstudiante, name='eliminarEstudiante')
]


    