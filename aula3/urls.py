
from django.urls import path, include
# from .views import index, setacookie, redireciona, show_code, redireciona_http_cats
from . import views
app_name = 'aula3'

# nunca import do arquivo 

urlpatterns = [
    path('', views.index),
    path('cookie', views.setacookie), #cookie criado
    path('uol', views.redireciona), #cookie criado
    path('<int:code>', views.show_code),
    path('cats/<int:code>', views.redireciona_http_cats),
    path('get/', views.show_get_values),
    path('post/', views.show_post_values),
]



