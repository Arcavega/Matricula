from django.shortcuts import render, redirect
from .forms import Formulario
from .models import Cadastro

# Create your views here.

def CadastroAluno(request):
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dados')
    else:
        print("Errou algo.")
        form = Formulario()

    return render(request, 'forms.html', {'form': form})

def Dados(request):
    alunos = Cadastro.objects.all()
    context = {
        'Cadastro': alunos
    }
    return render(request, "dados.html", context=context)