from django.urls import path
from modulos.views import index, pergunte, responda

urlpatterns = [
    path("", index, name="index"),
    path("pergunte/", pergunte, name="pergunte"),
    path("responda/", responda, name="responda"),
]
