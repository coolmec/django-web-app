from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Announce

# Create your views here.
def band_list(request):
    context = {}
    bands = Band.objects.all()
    context['bands'] = bands
    return render(request, 'listings/band_list.html', context)

def band_detail(request, band_id):
    context = {}
    band = Band.objects.get(id=band_id)
    context['band_id'] = band_id
    context['band'] = band
    return render(request, 'listings/band_detail.html', context)

def announce_list(request):
    context = {}
    bands = Band.objects.all()
    announces = Announce.objects.all()
    context['bands'] = bands
    context['announces'] = announces
    return render(request, 'listings/announce_list.html', context)

def announce_detail(request, announce_id):
    context = {}
    announce = Announce.objects.get(id=announce_id)
    context['announce_id'] = announce_id
    context['announce'] = announce
    return render(request, 'listings/announce_detail.html', context)

def contact_us(request):
    return HttpResponse("<h1>A propos</h1><p>Nous adorons merch !</p>")

