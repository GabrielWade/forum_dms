from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome de usuário:",
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "fundo__conteudo__caixa", 'placeholder': 'Ex.: Gabriel.Lima',}),
    )
    senha = forms.CharField(
        label="Senha:",
        max_length=50,
        widget=forms.PasswordInput(attrs={"class": "fundo__conteudo__caixa", 'placeholder': 'Digite sua senha'}),
    )