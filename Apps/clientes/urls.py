"""
from django.urls import path
from Apps.clientes.views import ClienteList, ClienteDetail

app_name = "clientes"
urlpatterns = [
    path('', ClienteList.as_view()),
    path('<int:pk>', ClienteDetail.as_view()),
]



#Envolviendo Vistas de Api
from django.urls import path
from Apps.clientes.views import cliente_list, cliente_detail

urlpatterns = [
    path('', cliente_list),
    path('<int:pk>/', cliente_detail),
]

"""

# Apps/clientes/urls.py

from django.urls import path
from Apps.clientes.views import ClienteList, ClienteDetail

urlpatterns = [
    path('', ClienteList.as_view(), name='cliente-list'),
    path('<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
]