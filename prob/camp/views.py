from django.shortcuts import render
from django.http import HttpResponse
from .models import Campeao
import cassiopeia as cass
from cassiopeia import Champions, Champion, Summoner


cass.set_riot_api_key("RGAPI-65099b18-8105-4a7c-ba30-9ce887fe6daf") 
cass.set_default_region("BR")
# Create your views here.


def index(request):
    try:
        return render(request, "camp/campeoes.html")
    except:
        return render(request, "camp/erro.html")

def build(request, nome):
    from .models import Campeao
    lista=[]
    
    for camp in Campeao.objects.all():
        lista.append(camp.nome)
    if nome in lista:
        camp=Campeao.objects.get(nome=nome)
        titulo=camp.titulo
        inicial1=camp.inicial1.riot_id
        inicial2=camp.inicial2.riot_id
        
        item1=camp.item1.riot_id
        item2=camp.item2.riot_id
        item3=camp.item3.riot_id
        item4=camp.item4.riot_id
        item5=camp.item5.riot_id
        item6=camp.item6.riot_id
        if camp.inicial3==None:
            pass
        else:
            inicial3=camp.inicial3.riot_id
            context={
            "nome":nome, "titulo":titulo, "inicial1":inicial1,
            "inicial2":inicial2, "inicial3":inicial3, "item1":item1,
            "item2":item2, "item3":item3, "item4":item4, "item5":item5,
            "item6":item6
        }
        context={
            "nome":nome, "titulo":titulo, "inicial1":inicial1,
            "inicial2":inicial2, "item1":item1,
            "item2":item2, "item3":item3, "item4":item4, "item5":item5,
            "item6":item6
        }
        return render(request, "camp/build.html", context)
        #return HttpResponse("Build padrao para %s" %nome)
    else:
        return render(request, "camp/erro.html")
    
    
