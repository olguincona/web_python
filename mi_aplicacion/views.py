from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("Hola Felipe")

def saludo_html(request):
    return HttpResponse("<b>Hola Felipe</b>")

def saludo_nombre(request, nombre):
    return HttpResponse(f"<h1>{nombre}</h1><br><b>Hola Felipe</b>")

def saludo_plantilla(request):
    contexto = {
        "nombre" : "Felipe",
        "edad" : 30,
        "curso" : "Python",
    }
    return render(request, "index.html", contexto)
