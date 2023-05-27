from django.shortcuts import render, redirect
from usuarios.forms import LoginForm
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login.')
            return redirect('login')
    return render(request, "usuarios/login.html", {"form": form})
