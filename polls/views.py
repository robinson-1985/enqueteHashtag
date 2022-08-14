#from django.shortcuts import render
from django.http import HttpResponse


#Tentativa de acessar o site
def index(request):
    return HttpResponse("Olá esse é o meu primeiro site!")
