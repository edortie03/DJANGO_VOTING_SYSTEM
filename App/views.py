from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("pentho")

def twahda(request):
    return HttpResponse("Ntagira")
def hadija(request):
    return HttpResponse("pendo")
def summy(request):
    return HttpResponse("payment")
