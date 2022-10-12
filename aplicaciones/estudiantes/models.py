from django.db import models

class grupo(models.Model):
    nombre = models.CharField(max_length=50)
    cant_estudiantes = models.PositiveIntegerField(blank=False,default=0)

class maestra(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    dependecia = models.PositiveIntegerField(blank=False,default=0)

class estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    #fecha_nacimiento = models.DateField(null=False)
    sexo = models.ForeignKey(maestra,related_name = 'sexo', null=True,on_delete = models.CASCADE)
    tipo_identificacion = models.ForeignKey(maestra,related_name = 'tipo_identificacion', null=True,on_delete = models.CASCADE)
    grupo = models.ForeignKey(grupo, on_delete = models.CASCADE)

class profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    sexo = models.ForeignKey(maestra,related_name = 'sexoP', null=True,on_delete = models.CASCADE)
    tipo_identificacion = models.ForeignKey(maestra,related_name = 'tipo_identificacionP', null=True,on_delete = models.CASCADE)

class asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.ForeignKey(profesor,on_delete = models.CASCADE)

class asignaturaXgrupo(models.Model):
    periodo_academico = models.PositiveIntegerField(blank=False, default=0)
    asignatura = models.ForeignKey(asignatura, on_delete = models.CASCADE)
    grupo = models.ForeignKey(grupo,on_delete = models.CASCADE)
    estudiante = models.ForeignKey(estudiante,on_delete = models.CASCADE)

class nota(models.Model):
    nota = models.FloatField(blank=False,default=0)
    logro = models.TextField(blank=False,default=0)
    asignaturaXgrupo = models.ForeignKey(asignaturaXgrupo, on_delete = models.CASCADE)












