from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('joke', views.joke, name="joke"),
    path('yes_answer', views.yes_answer , name="yes"),
    path('no_answer', views.no_answer , name="no"),
    path('kostya', views.kostya, name='kostya'),
    path('my_itmo', views.my_itmo, name='my_itmo'),
    path('be_itmo', views.be_itmo, name='be_itmo'),
]
