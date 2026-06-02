from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm

def index(request):

    view = request.GET.get("view", "pokemons")  # por defecto Pokémon

    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()

    if view == "pokemons":
        trainers = Trainer.objects.none()

    elif view == "trainers":
        pokemons = Pokemon.objects.none()

    return render(request, "index.html", {
        "pokemons": pokemons,
        "trainers": trainers,
        "view": view
    })

def pokemon(request, pokemon_id):
    pokemon_obj = get_object_or_404(Pokemon, id=pokemon_id)

    template = loader.get_template('display_pokemon.html')

    return HttpResponse(template.render({
        'pokemon': pokemon_obj
    }, request))


def trainer(request, trainer_id):
    trainer_obj = get_object_or_404(Trainer, id=trainer_id)

    template = loader.get_template('display_trainer.html')

    return HttpResponse(template.render({
        'trainer': trainer_obj
    }, request))


@login_required
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


@login_required
def edit_pokemon(request, pokemon_id):

    pokemon_obj = get_object_or_404(Pokemon, id=pokemon_id)

    if request.method == 'POST':

        form = PokemonForm(
            request.POST,
            request.FILES,
            instance=pokemon_obj
        )

        if form.is_valid():
            form.save()
            return redirect('/')

    else:

        form = PokemonForm(
            instance=pokemon_obj
        )

    return render(request, 'add_pokemon.html', {
        'form': form
    })


@login_required
def delete_pokemon(request, pokemon_id):

    pokemon_obj = get_object_or_404(
        Pokemon,
        id=pokemon_id
    )

    pokemon_obj.delete()

    return redirect('pokedex:index')


class CustomLoginView(LoginView):
    template_name = "login_form.html"


@login_required
def add_trainer(request):

    if request.method == 'POST':

        form = TrainerForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('pokedex:index')

    else:

        form = TrainerForm()

    return render(request, 'add_trainer.html', {
        'form': form
    })


@login_required
def edit_trainer(request, trainer_id):

    trainer_obj = get_object_or_404(
        Trainer,
        id=trainer_id
    )

    if request.method == 'POST':

        form = TrainerForm(
            request.POST,
            request.FILES,
            instance=trainer_obj
        )

        if form.is_valid():
            form.save()
            return redirect('pokedex:index')

    else:

        form = TrainerForm(
            instance=trainer_obj
        )

    return render(request, 'add_trainer.html', {
        'form': form
    })


@login_required
def delete_trainer(request, trainer_id):

    trainer_obj = get_object_or_404(
        Trainer,
        id=trainer_id
    )

    trainer_obj.delete()

    return redirect('pokedex:index')