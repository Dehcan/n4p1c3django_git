from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de app2</h1>")
def texto(request):
    return HttpResponse("<p>Soy un parrafo de la app2</p>")
def vista2(request):
    html="""
    <h1 style="color:orange">SOMOS TITERES DE APP2</h1>
    <h2>NADA MAS DE APP2</h2>
    """
    return HttpResponse(html)
# Create your views here.
