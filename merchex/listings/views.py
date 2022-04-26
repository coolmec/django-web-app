from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def listings(request):
    return HttpResponse("<h1>Hello World !</h1>")

def contact_us(request):
    return HttpResponse("<h1>A propos</h1><p>Nous adorons merch !</p>")

