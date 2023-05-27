from django.shortcuts import render, redirect
from modulos.models import Pergunta
from modulos.forms import PerguntaForm
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não está logado.")
        return redirect("login")
    return render(request, "modulos/index.html")


def pergunte(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não está logado.")
        return redirect("login")
    form = PerguntaForm(request.POST)
    if form.is_valid():
        pergunta = form["pergunta"].value()
        modulo = form["modulo"].value()
        Pergunta.objects.create(pergunta=pergunta, modulo=modulo)
        return redirect("index")
    
    return render(request, "modulos/pergunte.html", {"form": form})


def responda(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não está logado.")
        return redirect("login")
    perguntas = Pergunta.objects.all()  
    return render(request, "modulos/responda.html", {"linha": perguntas})

