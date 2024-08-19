from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de app1</h1>")
def vista1(request):
    html="""
    <h1 style="color:orange">SOMOS TITERES DE APP1</h1>
    <h2>NADA MAS DE APP1</h2>
    """
    return HttpResponse(html)
