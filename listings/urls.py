from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search',views.search, name='search'),
    path('price_asc',views.price_asc, name='price_asc'),
    path('year_desc',views.year_desc, name='year_desc'),
    path('year_asc',views.year_asc, name='year_asc'),
]