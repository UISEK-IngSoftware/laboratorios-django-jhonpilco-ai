from django.shortcuts import render, get_object_or_404
from .models import Pokemon

def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})


def pokemon(request, pokemon):
    pokemon_obj = get_object_or_404(Pokemon, name=pokemon)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon_obj})
