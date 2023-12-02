from django.shortcuts import render, redirect
from .models import cadastro
from .forms import CadastroForm





def pagina(request):
    form = CadastroForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista')
    else:
        return render(request, 'cadastro.html', {'form':form})
   

def sobre(request):
    return render(request, 'sobre.html')





def lista(request):
    pessoas = cadastro.objects.all()
    return render(request, 'lista.html',{'pessoas':pessoas})

