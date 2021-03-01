from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing, ListingForm
from listings.choice import price_choices, mileage_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    if request.method == 'GET':
        form = ListingForm(request.GET)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ListingForm()

    context = {
        'listings':listings,
        'price_choices' : price_choices,
        'mileage_choices': mileage_choices,
        'form': form,
    }
    return render(request, 'pages/index.html', context)
