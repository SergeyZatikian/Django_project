from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return(HttpResponse("<h4>Проверка работы</h4>"))
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123']
    }
    return(render(request, 'main/index.html', data))
def about(request):
    return(render(request, 'main/about.html'))
def joke(request):
    return(render(request, 'main/joke.html'))
def info_home(request):
    return(render(request, 'main/info_home.html'))