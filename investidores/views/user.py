from django.shortcuts import render, render_to_response # funcoes de renderizacao dos templates
from django.shortcuts import redirect # Funcao para executar um http-redirect

from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login, authenticate # funcao que salva o usuario na sessao
from investidores.forms import DesejoForm, CriaUsuarioForm, AutenticaUsuarioForm
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home.html')

   
# pagina de cadastro do usuario
def registrar(request):
    # Se dados forem passados via POST
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = CriaUsuarioForm(request.POST)
        
        if form.is_valid(): # se o formulario for valido
            user = form.save() # cria um novo usuario a partir dos dados enviados
            usuario_autenticado = authenticate(username=user.username, password=form.cleaned_data["password1"])
            if usuario_autenticado is not None:
                login(request,usuario_autenticado)
                return HttpResponseRedirect('/myadmin/investidores/desejo/') # redireciona o usuario logado para a lista de desejos
            
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "registrar.html", {"form": form})
   
    # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
    return render(request, "registrar.html", {"form": CriaUsuarioForm() })


# pagina de login do jogador
def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
        #form = AutenticaUsuarioForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            #agora, basta logar o usuario e ser feliz.
            login(request, form.get_user())
            return HttpResponseRedirect('/admin/investidores/desejo/') # redireciona o usuario logado para a lista de desejos
        else:
            return render(request, "logar.html", {"form": form})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "logar.html", {"form": AuthenticationForm()})
    #return render(request, "logar.html", {"form": AutenticaUsuarioForm()})