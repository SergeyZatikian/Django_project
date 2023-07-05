from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('joke', views.joke, name="joke"),
    path('info_home', views.info_home, name='info_home'),
]
