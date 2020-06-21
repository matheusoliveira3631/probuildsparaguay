from django.http import HttpResponse
from django.shortcuts import render
from camp.models import Campeao
import requests
import json
import ast
#o código mais podre e precario q eu já escrevi
def LimpaNome(nome):
    invalidos=["'",' ', '.']
    if nome=='Bardo':
        nomenovo='Bard'
        return nomenovo
    elif nome=='LeBlanc':
        nomenovo='Leblanc'
        return nomenovo
    elif nome=='Wukong':
        nomenovo='MonkeyKing'
        return nomenovo
    elif nome=='Nunu e Willump':
        nomenovo='Nunu'
        return nomenovo
    elif nome=="Cho'Gath":
        nomenovo='Chogath'
        return nomenovo
    elif nome=="Dr. Mundo":
        nomenovo='DrMundo'
        return nomenovo
    elif nome=="Kai'Sa":
        nomenovo='Kaisa'
        return nomenovo
    elif nome=="Kha'Zix":
        nomenovo='Khazix'
        return nomenovo
    elif nome=="Vel'Koz":
        nomenovo='Velkoz'
        return nomenovo
    for i in nome:
        if i in invalidos:
            nomelimpo=nome.replace(i,'')
            return nomelimpo
    else:
        return nome
################API da riot pega os campeao foda########################
    #teacher vai se fude
    #API key própria(atualizar toda semana q merdakkkkkkkkkkk)
riot_api_key=('RGAPI-65a4dd9c-9863-40e3-a1e6-bb36786aa111')
campeoes=Campeao.objects.all()

try :
    content=json.loads(requests.get("https://br1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=%s" %riot_api_key).content.decode('utf-8'))
    ftp_ids=content['freeChampionIds']
    ftp_nomes=[]
    for id in ftp_ids:
        camp=Campeao.objects.get(riot_key=str(id))
        dict={
            'nome':camp.nome,
            'nomelimpo':LimpaNome(camp.nome)
        }
        ftp_nomes.append(dict)
except:
    response=requests.get("https://br1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=%s" %riot_api_key)
    print("Could not reach Riot Games FTP API")
    print('Response status code: '+ str(response.status_code))
    #ftp stands for free to play champions (burropacarai)
#################top 5 challengers foda####################
def Get_ranked_data():
    ranks=json.loads(requests.get('https://br1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1&api_key=%s'%riot_api_key).content.decode('utf-8'))
    n=0
    player_data=[]
    while n<5:
        nome=ranks[n]['summonerName']
        pdl=ranks[n]['leaguePoints']
        request=requests.get('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=%s'%(ranks[n]['summonerName'], riot_api_key)).content.decode('utf-8')
        parse=json.loads(request)
        id_icone=parse['profileIconId']
        n+=1
        dict={
            'nome':nome,
            'pdl':pdl,
            'id':id_icone
        }
        player_data.append(dict)    
    return player_data

try:
    player_data=Get_ranked_data() 
except:
    print("Could not reach Riot games Ranked API")

##############status do servidor merda da riotkkkkkkkk###############
def Get_server_status():
    server_data=[]
    request=json.loads(requests.get('https://br1.api.riotgames.com/lol/status/v3/shard-data?api_key=%s'%riot_api_key).content.decode('utf-8'))
    services=request['services']
    n=0
    while n<4:
        nome=services[n]['name']
        status=services[n]['status']
        svs={
            'service_name':nome,
            'status':status
        }
        server_data.append(svs)
        n+=1
    return server_data

try:
    server_data=Get_server_status()
except:
    print('Could not reach Riot Games status API')
####################################################################

# Create your views here.
#Código que pega os campeões em rotação e passa como contexto pro html
def index(request):
    context={
        "ftp_nomes":ftp_nomes, 'player_data':player_data, 'server_data':server_data
    }
    return render(request, 'home\homepage.html', context)