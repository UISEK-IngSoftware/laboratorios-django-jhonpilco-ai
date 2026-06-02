from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),

    # Ver detalles
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>/", views.trainer, name="trainer"),

    # Pokémon
    path("add-pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit-pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete-pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),

    # Entrenadores
    path("add-trainer/", views.add_trainer, name="add_trainer"),
    path("edit-trainer/<int:trainer_id>/", views.edit_trainer, name="edit_trainer"),
    path("delete-trainer/<int:trainer_id>/", views.delete_trainer, name="delete_trainer"),

    # Autenticación
    path("login/", views.CustomLoginView.as_view(), name="login"),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),
]