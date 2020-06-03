from django.http import HttpResponse
from django.shortcuts import render
from camp.models import Campeao
import requests
import ast

################API da riot pega os campeao fodas##################
################teacher vai se fude#########################
#API key própria(atualizar toda semana q merdakkkkkkkkkkk)
riot_api_key=('RGAPI-b839f6a9-4299-41a0-a21c-306d4a708018')
campeoes=Campeao.objects.all()
response=requests.get("https://br1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=%s" %riot_api_key)
conteudo=response.content
decode=ast.literal_eval(conteudo.decode('utf-8'))
ftp_ids=decode['freeChampionIds']
ftp_nomes=[]
for id in ftp_ids:
    camp=Campeao.objects.get(riot_key=str(id))
    ftp_nomes.append(camp.nome.replace(' ',''))

#ftp stands for free to play champions (burropacarai)
################zapzap#####################################


# Create your views here.
#Código que pega os campeões em rotação e passa como contexto pro html
def index(request):
    context={
        "ftp_nomes":ftp_nomes
    }
    return render(request, 'home\homepage.html', context)