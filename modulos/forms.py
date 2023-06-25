from django import forms
from django.forms.widgets import SelectMultiple

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

class PerguntaForm(forms.Form):
    modulo = forms.MultipleChoiceField(
        label="Qual módulo é sua dúvida?",
        choices=MODULOS,
        widget=SelectMultiple(attrs={"class": "select2"}),
    )
    
    pergunta = forms.CharField(
        label="Faça sua pergunta",
        required=True,
        widget=forms.TextInput(attrs={"class": "pergunte__conteudo__caixa", 'placeholder': 'Ex.: O que é CRM?'}),
    )

class RespondaForm(forms.Form):
    resposta = forms.CharField(
        label="Resposta:",
        required=True,
        widget=forms.Textarea(attrs={"class":"form-control", "id":"exampleFormControlTextarea1", "rows":"3"}),
    )
