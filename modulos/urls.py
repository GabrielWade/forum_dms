from django.urls import path
from modulos.views import index, pergunte, responda, respondaPergunta

urlpatterns = [
    path("", index, name="index"),
    path("pergunte/", pergunte, name="pergunte"),
    path("responda/", responda, name="responda"),
    path("respondaPergunta/<int:pergunta_id>", respondaPergunta, name="respondaPergunta")
]
