
from django.urls import path, include
from .views import index, setacookie, redireciona
app_name = 'aula3'

# nunca import do arquivo 

urlpatterns = [
    path('', index),
    path('cookie', setacookie), #cookie criado
    path('uol', redireciona), #cookie criado
]



