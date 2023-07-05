from django.shortcuts import render

def info_home(request):
    return(render(request, 'main/info_home.html'))