from django.contrib import admin
from modulos.models import Pergunta

class ListandoPerguntas(admin.ModelAdmin):
    list_display = ("id", "modulo", "pergunta")
    list_display_links = ("id", "modulo", "pergunta")
    search_fields = ("pergunta",)
    list_filter = ("modulo",)

admin.site.register(Pergunta, ListandoPerguntas)
