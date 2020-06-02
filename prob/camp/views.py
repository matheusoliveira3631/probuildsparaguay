from django.shortcuts import render
from django.http import HttpResponse
from .models import Campeao
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
            inicial3="3340"
        else:
            inicial3=camp.inicial3.riot_id
        context={
            "nome":nome, "titulo":titulo, "inicial1":inicial1,
            "inicial2":inicial2, "inicial3":inicial3, "item1":item1,
            "item2":item2, "item3":item3, "item4":item4, "item5":item5,
            "item6":item6
        }
        return render(request, "camp/build.html", context)
    else:
        return render(request, "camp/erro.html")
    
    
