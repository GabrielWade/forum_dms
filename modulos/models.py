from django.db import models
from multiselectfield import MultiSelectField

class Pergunta(models.Model):
    MODULOS = [
        ("Cad. Basico", "Cad. Basico"),
        ("Pricing", "Pricing"),
        ("CRM", "CRM"),
        ("PM", "PM"),
        ("Operations", "Operations"),
        ("DWSYS", "DWSYS"),
        ("CLR", "CLR"),
        ("DLC", "DLC"),
        ("Financial", "Financial"),
        ("Chamados", "Chamados"),
        ("OKR", "OKR"),
        ("All", "All"),
    ]
    modulo = MultiSelectField(choices=MODULOS, max_choices=12, max_length=200, default="All")
    pergunta = models.TextField(null=False, blank=False)
    respondida = models.BooleanField(default=False)

    def __str__(self):
        return f"Pergunta [pergunta={self.pergunta}]"


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    resposta = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Resposta [pergunta={self.pergunta.pergunta}]"
