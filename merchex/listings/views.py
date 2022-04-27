from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Announce

# Create your views here.
def hello(request):
    context = {}
    bands = Band.objects.all()
    context['bands'] = bands
    return render(request, 'hello.html', context)


def listings(request):
    bands = Band.objects.all()
    announces = Announce.objects.all()
    return HttpResponse(f"""
                        <h1>Hello World !</h1>
                        <p>Mes groupes préférés sont :</p>
                        <ul>
                            <li>{bands[0].name}</li>
                            <li>{bands[1].name}</li>
                            <li>{bands[2].name}</li>
                        </ul>
                        <p>Les annonces disponibles:</p>
                        <ul>
                            <li>{announces[0].title}</li>
                            <li>{announces[1].title}</li>
                            <li>{announces[2].title}</li>
                        </ul>
                        """)


def contact_us(request):
    return HttpResponse("<h1>A propos</h1><p>Nous adorons merch !</p>")

