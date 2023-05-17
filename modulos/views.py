from django.shortcuts import render


def index(request):
    return render(request, "modulos/index.html")


def pergunte(request):
    return render(request, "modulos/pergunte.html")
