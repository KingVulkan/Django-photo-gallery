from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from django.http import Http404
from django.shortcuts import render,redirect
from .models import Image,Category,Location

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def gallery_today(request):
    date = dt.date.today()
    gallery = Image.today_gallery()        
    return render(request, 'all_gallery/today-gallery.html', {"date": date,"gallery":gallery})

def convert_dates(dates):
    #function that gets the weekday number for the date
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #returning the actual day of the week
    day = days[day_number]
    return day 

def past_days_gallery(request,past_date):

    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        raise Http404()    
    #converts data from the string url
    if date == dt.date.today():
        return redirect (gallery_today)
    
    gallery = Image.days_gallery(date)
    return render(request, 'all-gallery/past-gallery.html',{"date": date,"gallery": gallery})

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_gallery/search.html',{"message":message,"images": searched_images})
    else:
        message = "you haven't searched for any term"
        return render(request, 'all_gallery/search.html',{"message":message})  

def category_image(request):
    gallery = Category.images()   
    for x in gallery:
        print(x.image_upload)    
    return render(request, 'all_gallery/category.html', {"gallery":gallery})

def location(request,location_id):
    locations = Image.objects.filter(location_id=location_id)
    return render(request, 'all_gallery/location.html', {"locations":locations})

