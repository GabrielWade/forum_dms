from django.shortcuts import render, redirect, get_object_or_404
from modulos.models import Pergunta, Resposta
from modulos.forms import PerguntaForm, RespondaForm, VerificaForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
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
        usuario = request.user
        Pergunta.objects.create(pergunta=pergunta, modulo=modulo, usuario=usuario)
        return redirect("index")
    
    return render(request, "modulos/pergunte.html", {"form": form})


def responda(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não está logado.")
        return redirect("login")

    object_list = Pergunta.objects.order_by("-data_pergunta").all()
    search = request.GET.get('search')

    if search:
        object_list = object_list.filter(
            Q(modulo__icontains=search)
            | Q(pergunta__icontains=search)
        )
        return render(request, "modulos/searchResult.html", {"object_list": object_list})
    else:
        perguntas = Pergunta.objects.order_by("-data_pergunta").all()
        return render(request, "modulos/responda.html", {"linha": perguntas})

    paginator = Paginator(object_list, 10)  # Defina o número de itens por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "modulos/responda.html", {"linha": page_obj})


def respondaPergunta(request, pergunta_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não está logado.")
        return redirect("login")

    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    if request.method == "POST":
        form_resposta = RespondaForm(request.POST)
        form_verifica = VerificaForm(request.POST)
        if form_resposta.is_valid():
            resposta_texto = form_resposta.cleaned_data["resposta"]
            Resposta.objects.create(pergunta=pergunta, resposta=resposta_texto)
            return redirect("respondaPergunta", pergunta_id=pergunta.id)
        elif form_verifica.is_valid():
            pergunta.respondida = form_verifica.cleaned_data['verificaResposta']
            pergunta.save()
            return redirect("respondaPergunta", pergunta_id=pergunta.id)
    else:
        form_resposta = RespondaForm()
        form_verifica = VerificaForm(initial={'verificaResposta': pergunta.respondida})

    return render(request, "modulos/respondaPergunta.html", {"pergunta": pergunta, "form_resposta": form_resposta, "form_verifica": form_verifica})

