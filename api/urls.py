from django.urls import path, include
from rest_framework import routers
from .views import PokemonViewSet, TrainerViewSet

router = routers.DefaultRouter()

router.register("pokemons", PokemonViewSet)
router.register("trainers", TrainerViewSet)

urlpatterns = [
    path("", include(router.urls))
]