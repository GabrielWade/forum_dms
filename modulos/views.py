from django.shortcuts import render, redirect, get_object_or_404
from modulos.models import Pergunta, Resposta
from modulos.forms import PerguntaForm, RespondaForm
from django.contrib import messages
from django.db.models import Q
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

    object_list = Pergunta.objects.all()
    search = request.GET.get('search')

    if search:
        object_list = object_list.filter(
            Q(modulo__icontains=search)
            | Q(pergunta__icontains=search)
        )
        return render(request, "modulos/searchResult.html", {"object_list": object_list})
    else:
        perguntas = Pergunta.objects.all()
        return render(request, "modulos/responda.html", {"linha": perguntas})

def respondaPergunta(request, pergunta_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não está logado.")
        return redirect("login")

    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    if request.method == "POST":
        form = RespondaForm(request.POST)
        if form.is_valid():
            resposta_texto = form.cleaned_data["resposta"]
            Resposta.objects.create(pergunta=pergunta, resposta=resposta_texto)
            return redirect("respondaPergunta", pergunta_id=pergunta.id)
    else:
        form = RespondaForm()

    return render(request, "modulos/respondaPergunta.html", {"pergunta": pergunta, "form": form})

