from django.shortcuts import render
from django.views.generic import ListView
from .models import RestaurantInfo, About, Gallery
from menu.models import MenuItem

def home(request):
    """Home page view"""
    try:
        restaurant_info = RestaurantInfo.objects.first()
    except RestaurantInfo.DoesNotExist:
        restaurant_info = None
    
    # Get popular menu items
    popular_items = MenuItem.objects.filter(is_popular=True, is_active=True)[:6]
    
    # Get latest gallery images
    gallery_images = Gallery.objects.all()[:8]
    
    context = {
        'restaurant_info': restaurant_info,
        'popular_items': popular_items,
        'gallery_images': gallery_images,
    }
    return render(request, 'core/index.html', context)

def about(request):
    """About page view"""
    try:
        about_content = About.objects.first()
    except About.DoesNotExist:
        about_content = None
    
    try:
        restaurant_info = RestaurantInfo.objects.first()
    except RestaurantInfo.DoesNotExist:
        restaurant_info = None
    
    context = {
        'about_content': about_content,
        'restaurant_info': restaurant_info,
    }
    return render(request, 'core/about.html', context)

class GalleryView(ListView):
    """Gallery page view"""
    model = Gallery
    template_name = 'core/gallery.html'
    context_object_name = 'gallery_images'
    paginate_by = 12
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['restaurant_info'] = RestaurantInfo.objects.first()
        except RestaurantInfo.DoesNotExist:
            context['restaurant_info'] = None
        return context
