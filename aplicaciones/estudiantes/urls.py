from . import views
from django.urls import path

urlpatterns =[
    path('',views.index,name='index'),
    path('contactanos/',views.contactanos,name='contactanos'),
    path('contactanos/index/',views.index, name="index"),
    path('listarEstudiantes/',views.listarEstudiantes,name='listarEstudiantes'),
    path('nosotros/',views.nosotros,name ='nosotros')
]


    