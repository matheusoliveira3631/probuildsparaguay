from django.shortcuts import render
from django.http import HttpResponse
from .models import Campeao
from .models import Item
from .models import Spell
# Create your views here.


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
##############################################
#passando os campeões p/ o render
def Get_champions():
    camps=[]
    objetos=Campeao.objects.all()
    for campeao in objetos:
        dict={
            'nomelimpo':LimpaNome(campeao.nome),
            'nome':campeao.nome,
            'titulo':campeao.titulo
        }
        camps.append(dict)
    return camps
##############################################
def index(request):   
    try:
        camps=Get_champions()
        context={
            'camps':camps
        }
        return render(request, "camp/campeoes.html", context )
    except:
        return render(request, "camp/erro.html")



def build(request, nome):
    try:
        campeao=Campeao.objects.get(nome=nome)
        if campeao.inicial3==None:
            campeao.inicial3=Item.objects.get(riot_id='3340')
        info={
            'nomelimpo':LimpaNome(campeao.nome),
            'nome':campeao.nome,
            'titulo':campeao.titulo,
            'tipo':campeao.tipo
        }
        ##
        inicial1=campeao.inicial1.riot_id
        inicial2=campeao.inicial2.riot_id
        inicial3=campeao.inicial3.riot_id
        iniciais=[inicial1, inicial2, inicial3]
        ## 
        item1=campeao.item1.riot_id
        item2=campeao.item2.riot_id
        item3=campeao.item3.riot_id
        item4=campeao.item4.riot_id
        item5=campeao.item5.riot_id
        item6=campeao.item6.riot_id
        early=[item1,item2,item3]
        late=[item4,item5,item6]
        full=early+late
        ##
        spells={
            'qspell':{
                'nome':campeao.qspell.nome,
                'desc':campeao.qspell.desc,
                'id':campeao.qspell.spell_id,
                'link':campeao.qspell.video_link
            },
            'wspell':{
                'nome':campeao.wspell.nome,
                'desc':campeao.wspell.desc,
                'id':campeao.wspell.spell_id,
                'link':campeao.wspell.video_link
            },
            'espell':{
                'nome':campeao.espell.nome,
                'desc':campeao.espell.desc,
                'id':campeao.espell.spell_id,
                'link':campeao.espell.video_link
            },
            'rspell':{
                'nome':campeao.rspell.nome,
                'desc':campeao.rspell.desc,
                'id':campeao.rspell.spell_id,
                'link':campeao.rspell.video_link
            }
        }        
        context={
            'info':info, 'iniciais':iniciais, 'early':early, 'late':late,
            'full':full, 'spells':spells
        }
        return render(request, "camp/build.html", context)
    except:
        return render(request, "camp/erro.html")
    
    
