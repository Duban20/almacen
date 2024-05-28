from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('correoCliente',)  # No permite edición de create y update
    list_display = ('nombreCliente', 'direccionCliente', 'telefonoCliente', 'correoCliente')
    ordering = ('nombreCliente', 'direccionCliente', 'correoCliente')  # En caso que sea una sola ordering('column',)
    search_fields = ('nombreCliente', 'correoCliente')  # Campo relacionado
    list_filter = ('nombreCliente', 'correoCliente', 'direccionCliente')  # Campos relacionados

admin.site.register(Cliente, ClienteAdmin)


