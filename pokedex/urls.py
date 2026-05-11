from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<str:pokemon>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>/", views.trainer, name="trainer"),

    path('add-pokemon/', views.add_pokemon, name='add_pokemon'),
]