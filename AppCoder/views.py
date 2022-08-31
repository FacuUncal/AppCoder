from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.
def curso(request):
    curso=Curso(nombre='AWS', comision=31105)
    curso1=Curso(nombre='Lengua', comision=1)
    curso2=Curso(nombre='Mat', comision=2)
    curso.save()
    curso1.save()
    curso2.save()
    texto=f'Cursos creados'
    return HttpResponse(texto)

def inicio(request):
    return HttpResponse(('Inicio'))

def cursos(request):
    return HttpResponse(('Cursos'))

def estudiantes(request):
    return HttpResponse(('Estudiantes'))

def profesores(request):
    return HttpResponse(('Profesores'))

def entregables(request):
    return HttpResponse(('Entregables'))
