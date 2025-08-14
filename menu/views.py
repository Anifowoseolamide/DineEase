from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, MenuItem
from core.models import RestaurantInfo

class MenuListView(ListView):
    """View for displaying all menu categories"""
    model = Category
    template_name = 'menu/menu_list.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return Category.objects.filter(is_active=True).prefetch_related('menu_items')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['restaurant_info'] = RestaurantInfo.objects.first()
        except RestaurantInfo.DoesNotExist:
            context['restaurant_info'] = None
        return context

class MenuDetailView(DetailView):
    """View for displaying individual menu item details"""
    model = MenuItem
    template_name = 'menu/menu_detail.html'
    context_object_name = 'menu_item'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['restaurant_info'] = RestaurantInfo.objects.first()
        except RestaurantInfo.DoesNotExist:
            context['restaurant_info'] = None
        
        # Get related items from the same category
        if self.object.category:
            context['related_items'] = MenuItem.objects.filter(
                category=self.object.category,
                is_active=True
            ).exclude(id=self.object.id)[:4]
        
        return context

def category_detail(request, slug):
    """View for displaying all items in a specific category"""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    menu_items = MenuItem.objects.filter(category=category, is_active=True)
    
    try:
        restaurant_info = RestaurantInfo.objects.first()
    except RestaurantInfo.DoesNotExist:
        restaurant_info = None
    
    context = {
        'category': category,
        'menu_items': menu_items,
        'restaurant_info': restaurant_info,
    }
    return render(request, 'menu/menu_list.html', context)
