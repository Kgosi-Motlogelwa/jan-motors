from django.shortcuts import get_object_or_404 , render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing, ListingForm
from .choice import price_choices, mileage_choices

# Create your views here.
def index(request):
    listings= Listing.objects.order_by('-price').filter(is_published = True)

    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings,
        'price_choices' : price_choices,
        'mileage_choices': mileage_choices,
    }
    return render(request, 'listings/listings.html', context)

def price_asc(request):
    listings= Listing.objects.order_by('price').filter(is_published = True)

    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings,
        'price_choices' : price_choices,
        'mileage_choices': mileage_choices,
    }
    return render(request, 'listings/listings.html', context)

def year_desc(request):
    listings= Listing.objects.order_by('-year').filter(is_published = True)

    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings,
        'price_choices' : price_choices,
        'mileage_choices': mileage_choices,
    }
    return render(request, 'listings/listings.html', context)

def year_asc(request):
    listings= Listing.objects.order_by('year').filter(is_published = True)

    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings,
        'price_choices' : price_choices,
        'mileage_choices': mileage_choices,
    }
    return render(request, 'listings/listings.html', context)



def listing(request, listing_id):
    listing_var = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing_var
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    # Bringing over listings from listings.model - Listing 
    queryset_list = Listing.objects.order_by('-list_date')




    
    if request.method == 'GET':
        form = ListingForm(request.GET)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ListingForm()
    # Search for keywords
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords: # 'if' Checks if empty string
        queryset_list = queryset_list.filter(description__icontains=keywords)  # Does the paragraph/description contain this set of keywords

    # Year 
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            queryset_list = queryset_list.filter(year__gte=year)

    # Model/Brand 
    if 'brand_model' in request.GET:
        brand_model = request.GET['brand_model']
        if brand_model:
            queryset_list = queryset_list.filter(brand_model__iexact=brand_model)

     # Body Type 
    if 'body_type' in request.GET:
        body_type = request.GET['body_type']
        if body_type:
            queryset_list = queryset_list.filter(body_type__iexact=body_type)

    # Dealership 
    if 'dealership' in request.GET:
        dealership = request.GET['dealership']
        if dealership:
            queryset_list = queryset_list.filter(dealership__iexact=dealership)
    # Fuel Type 
    if 'fuel_type' in request.GET:
        fuel_type = request.GET['fuel_type']
        if fuel_type:
            queryset_list = queryset_list.filter(fuel_type__iexact=fuel_type)
    # Price 
    # Trying to show range bigger (gte) than the one selected but smaller that the one above]
    price_choices_list = ['0','30000','50000','70000','100000','150000','200000','300000','400000','500000']
    
    if 'price' in request.GET:
        price = request.GET['price']
        append = 0
        next_price =  10000000
        for x in price_choices_list:
            if append == 1:
                next_price = x
                break 
            if x == price and append == 0:
                append = 1
        if price:
            queryset_list = queryset_list.filter(price__gte=price, price__lt=next_price)

    # Mileage 
    # Trying to show range bigger (gte) than the one selected but smaller that the one above]
    mileage_list = ['0','20000','50000','100000','150000','200000']
    
    if 'mileage' in request.GET:
        mileage = request.GET['mileage']
        append = 0
        next_mileage =  10000000
        for x in mileage_list:
            if append == 1:
                next_mileage = x
                break 
            if x == mileage and append == 0:
                append = 1

        if mileage:
            queryset_list = queryset_list.filter(mileage__gte=mileage, mileage__lt=next_mileage)

    listing_price_desc = queryset_list.order_by('-price') 
    listing_price_asc = queryset_list.order_by('price')
    listing_year_desc = queryset_list.order_by('-year')
    listing_year_asc = queryset_list.order_by('year')


    context = {
        'listings': queryset_list,
        'listing_price_desc': listing_price_desc,
        'listing_price_asc': listing_price_asc,
        'listing_year_desc': listing_year_desc,
        'listing_year_asc': listing_year_asc,
        'price_choices' : price_choices,
        'mileage_choices': mileage_choices,
        'values': request.GET,
        'form': form,
    }
    return render(request, 'listings/search.html', context)
    