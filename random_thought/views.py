from django.shortcuts import render, redirect, get_object_or_404

from random_thought.forms import AddThought
from random_thought.models import Thought
from random import randint


# Create your views here.

def random(request):
    count = Thought.objects.all().count()
    random_object = Thought.objects.all()[randint(0, count - 1)]
    return render(
        request,
        'random_thought/thought.html',
        context={
            'random': random_object,
        }
    )


def add(request):
    if request.method == "POST":
        form = AddThought(request.POST)  # bound form

        if form.is_valid():
            form.save()

        return redirect('random_thought:list-thought')

    form = AddThought()  # unbound form
    return render(
        request,
        'random_thought/add_thought.html',
        context={
            'form': form
        }
    )


def list_view(request):
    thought = Thought.objects.all()

    return render(
        request,
        'random_thought/list_thought.html',
        context={
            'thought': thought,
        }
    )


def detail(request, pk):
    thought = get_object_or_404(Thought, pk=pk)
    return render(
        request,
        'random_thought/detail_thought.html',
        context={
            'thought': thought,
        }
    )


def update(request, pk):
    thought = get_object_or_404(Thought, pk=pk)

    if request.method == "POST":
        form = AddThought(request.POST, instance=thought)
        if form.is_valid():
            form.save()
            return redirect('random_thought:list-thought')

    else:
        form = AddThought(instance=thought)

    return render(
        request,
        'random_thought/add_thought.html',
        context={
            'form': form
        }
    )


def delete(request, pk):
    thought_to_del = get_object_or_404(Thought, pk=pk)
    if request.method == "POST":
        thought_to_del.delete()
        return redirect('random_thought:list-thought')

    return render(
        request,
        'random_thought/detail_thought.html',
        context={
            'thought_to_del': thought_to_del,
        }
    )
