from django.contrib import admin
from .models import Venta, VentaProducto

class MembershipInline(admin.TabularInline):
    model = VentaProducto
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

admin.site.register(Venta, VentaAdmin)
