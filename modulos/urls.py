from django.urls import path
from modulos.views import index, pergunte

urlpatterns = [
    path("", index, name="index"),
    path("pergunte/", pergunte, name="pergunte"),
]
