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
def yes_answer(request):
    return(render(request, 'main/yes_answer.html'))
def no_answer(request):
    return(render(request, 'main/no_answer.html'))
def kostya(request):
    return(render(request, 'main/kostya.html'))
def my_itmo(request):
    return(render(request, 'main/my_itmo.html'))
def be_itmo(request):
    return(render(request, 'main/be_itmo.html'))