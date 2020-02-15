from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone # tem que pegar o time zone pq o servidor pode ser com fusohorario diferente
from django.conf import settings



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




