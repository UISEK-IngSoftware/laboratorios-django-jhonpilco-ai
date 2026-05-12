from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import render, redirect
from .forms import PokemonForm


def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()

    template = loader.get_template('index.html')

    return HttpResponse(template.render({
        'pokemons': pokemons,
        'trainers': trainers
    }, request))


def pokemon(request, pokemon_id):
    pokemon_obj = Pokemon.objects.get(id=pokemon_id)

    template = loader.get_template('display_pokemon.html')

    return HttpResponse(template.render({
        'pokemon': pokemon_obj
    }, request))


def trainer(request, trainer_id):
    trainer_obj = Trainer.objects.get(id=trainer_id)

    template = loader.get_template('display_trainer.html')

    return HttpResponse(template.render({
        'trainer': trainer_obj
    }, request))


def add_pokemon(request):

    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = PokemonForm()

    return render(request, 'add_pokemon.html', {
        'form': form
    })


def edit_pokemon(request, pokemon_id):

    pokemon_obj = Pokemon.objects.get(id=pokemon_id)

    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon_obj)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = PokemonForm(instance=pokemon_obj)

    return render(request, 'add_pokemon.html', {
        'form': form
    })

from django.shortcuts import get_object_or_404, redirect

def delete_pokemon(request, pokemon_id):
    try:
        pokemon_obj = Pokemon.objects.get(id=pokemon_id)
        pokemon_obj.delete()
    except Pokemon.DoesNotExist:
        pass  # o mostrar mensaje
    return redirect('pokedex:index')