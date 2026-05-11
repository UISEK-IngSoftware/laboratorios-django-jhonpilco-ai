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


def pokemon(request, pokemon):
    pokemon_obj = Pokemon.objects.get(name=pokemon)

    template = loader.get_template('display_pokemon.html')

    context = {
        'pokemon': pokemon_obj
    }

    return HttpResponse(template.render(context, request))


def trainer(request, trainer_id):
    trainer_obj = Trainer.objects.get(id=trainer_id)

    template = loader.get_template('display_trainer.html')

    context = {
        'trainer': trainer_obj
    }

    return HttpResponse(template.render(context, request))

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