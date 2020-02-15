from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone # tem que pegar o time zone pq o servidor pode ser com fusohorario diferente
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt



def index(request):
    html = '<h1>bem vindo</h1>'
    response = HttpResponse(html, status=404) #podemos passar o status junto da resposta 
    response['ultimo_acesso'] = timezone.now() #pega data e hora atual
    # response['ultimo_acesso'] = 'lucas'
    # response['ultimo_acesso'] = timezone.localtime(timezone.now()) #pega data e hora atual erro

    return response 

#  criando um cookie novo
def setacookie(request):

    response = HttpResponse()
    response.set_cookie('my_name', value = "Lucas")
    return response


def redireciona(request):
    return HttpResponseRedirect('http://uol.com.br')


def show_code(request, code):
    html = f'<h1> o código e {code}</h1>'
    response = HttpResponse(html)
    return response 



# https://http.cat/200


def redireciona_http_cats(request, code):
        return HttpResponseRedirect(f'https://http.cat/{code}')


def show_get_values(request):
    # import ipdb; ipdb.set_trace()
    nome = request.GET.get('nome' , None) # pegando atributos da request
    if nome is None:
        html = f'<h1>bem vindo usuário anônimo</h1>'
    else:
        html = f'<h1>bem vindo {nome}</h1>'
    return HttpResponse(html)

@csrf_exempt
def show_post_values(request):
    head = ''
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        head = f'<h1>bem vindo {nome} {sobrenome}</h1>'


    html = """


    <form method="POST">

    <label for="fname">First name:</label><br>
    <input type="text" id="nome" name="nome" value="John"><br>
    <label for="lname">Last name:</label><br>
    <input type="text" id="sobrenome" name="sobrenome" value="Doe"><br><br>
    <input type="submit" value="Enviar">
    </form> 

    """
    html_to_reponse = head + html
    return HttpResponse(html_to_reponse)



