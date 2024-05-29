from rest_framework import serializers
from Apps.ventas.models import Venta

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = "__all__"

    def validate_nombreVenta(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Nombre no puede ser tan corto')
        else:
            return value

    def validate_precioVenta(self, value):
        if value <= 0:
            raise serializers.ValidationError('El precio debe ser mayor que 0')
        else:
            return value
        

# Filtros y busqueda
from rest_framework import serializers
from Apps.ventas.models import Venta, VentaProducto

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class VentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaProducto
        fields = '__all__'
