from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenidos a la aplicación de Ventas")

