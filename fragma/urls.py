from django.urls import path
from .views import lista
from .views import pagina
from .views import sobre


urlpatterns = [
    path('',lista, name='lista'),
    path('cadastro/', pagina, name='pagina'),
    path('sobre/', sobre, name='sobre')
      
]

