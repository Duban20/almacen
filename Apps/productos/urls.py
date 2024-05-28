from django.urls import path
from .views import home

urlpatterns = [
    path('inicio/', home, name='home'),
]



# configuracion de la URL de la API
from django.urls import path
from Apps.productos.views import ProductoView

app_name = "productos"
urlpatterns = [
    path('', ProductoView.as_view()),
]
