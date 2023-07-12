from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.logar, name="login"),
    path('home/', views.home, name="home"),
    path('addTreinador', views.addTreinador, name="addTreinador"),
    path('addItens/', views.addItens, name="addItens"),
    path('delete-pokemon/<int:pokemon_id>/', views.deletePokemon, name='deletePokemon'),
    path('visao/', views.visao, name="visao"),
]