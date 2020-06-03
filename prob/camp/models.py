from django.db import models
###############################################
#teacher vai toma no cu
###############################################
# Create your models here.

class Item(models.Model):
    nome=models.CharField(max_length=200,null=True,blank=False, default="Sem Item")
    riot_id=models.CharField(max_length=255, blank=False, default=3916)
    def __str__(self):
        return self.nome



class Campeao(models.Model):
    nome=models.CharField(max_length=200,blank=False)
    titulo=models.CharField(max_length=255, blank=False, default="Título")
    riot_key=models.CharField(max_length=10, null=False, blank=True, default='0')
    inicial1=models.ForeignKey(Item,null=True,related_name='inicial1', on_delete=models.SET_NULL)
    inicial2=models.ForeignKey(Item,null=True,related_name='inicial2', on_delete=models.SET_NULL)
    inicial3=models.ForeignKey(Item,null=True,related_name='inicial3', on_delete=models.SET_NULL)
    item1=models.ForeignKey(Item,null=True,related_name='item1', on_delete=models.SET_NULL)
    item2=models.ForeignKey(Item,null=True,related_name='item2', on_delete=models.SET_NULL)
    item3=models.ForeignKey(Item,null=True,related_name='item3', on_delete=models.SET_NULL)
    item4=models.ForeignKey(Item,null=True,related_name='item4', on_delete=models.SET_NULL)
    item5=models.ForeignKey(Item,null=True,related_name='item5', on_delete=models.SET_NULL)
    item6=models.ForeignKey(Item, null=True, related_name='item6', on_delete=models.SET_NULL)
    def __str__(self):
        return self.nome

    
