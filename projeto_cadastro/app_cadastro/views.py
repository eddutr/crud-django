from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,"usuarios\home.html")

def usuarios(request):
    # salvar dados da tela para o banco
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # exibir usuarios ja cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # retornar dados para staging page
    return render(request,"usuarios\\usuarios_pag.html",usuarios)