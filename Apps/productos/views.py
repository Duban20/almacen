from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Bienvenidos a la aplicación de Productos")


# API View
from rest_framework.response import Response
from rest_framework.views import APIView

from Apps.productos.models import Producto, TipoProducto

class ProductoView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        return Response({"productos": productos})
    


# Actualización de la Vista de la API
from .serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Producto

class ProductoView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    




