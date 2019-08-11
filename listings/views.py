from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Listing
from .choices import price_choices, state_choices, bedroom_choices

# Create your views here.
def index(request): #all listings
    #fetching the listings from DB
    #listings = Listing.objects.all()

    #fetching the listings from DB, ordered by a field value, and filtered by a field value 
    listings = Listing.objects.order_by('-list_date').filter(is_published = True) # 'fieldname' for ascending order, '-fieldname' for descending order

    paginator = Paginator(listings,6) #create a paginator passing the objects and how many of them we want per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    #we need to pass the listings as a dictionary, is more practical to store it in a variable and then pass it
    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context) 

def listing(request, listing_id): #indiviual listing
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing' : listing
    }
    return render(request, 'listings/listing.html', context)

def search(request): 
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'] # request.GET fetches the 'value' of the html object of 'name' = 'keywords'
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords) # 'description' is one of our DB fields, '__icontains' searches in our field for a match, the 'i' in 'icontains' makes it not case sensitive

    # city
    if 'city' in request.GET:
        city = request.GET['city'] # request.GET fetches the 'value' of the html object of 'name' = 'city'
        if city:
            queryset_list = queryset_list.filter(city__iexact = city) # 'city' is one of our DB fields, '__iexact' searches in our field for an exact match, again the 'i' in 'iexact' makes it not case sensitive
    
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact = state) 
    
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms) # '__lte' : less than or equal to. We want to show the listings, with the bedrooms up to the amount searched for
    
    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price) 

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)