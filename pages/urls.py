from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    #path('about',views.about, name='about'),
    #path('gaborone',views.gaborone, name='gaborone'),
    #path('palapye',views.palapye, name='palapye'),

]