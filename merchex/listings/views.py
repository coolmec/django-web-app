from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Announce

# Create your views here.
def band_list(request):
    context = {}
    bands = Band.objects.all()
    context['bands'] = bands
    return render(request, 'listings/band_list.html', context)


def listings(request):
    context = {}
    bands = Band.objects.all()
    announces = Announce.objects.all()
    context['bands'] = bands
    context['announces'] = announces
    return render(request, 'listings/band_list.html', context)


def contact_us(request):
    return HttpResponse("<h1>A propos</h1><p>Nous adorons merch !</p>")

