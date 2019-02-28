from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$',views.gallery_today,name='galleryToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_gallery,name = 'pastGallery'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/$',views.category_image,name='categorysToday'),
    url(r'^location/(\d+)',views.location,name='location'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
