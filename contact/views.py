from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import ContactMessage
from .forms import ContactForm
from core.models import RestaurantInfo

class ContactCreateView(CreateView):
    """View for contact form"""
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact_success')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['restaurant_info'] = RestaurantInfo.objects.first()
        except RestaurantInfo.DoesNotExist:
            context['restaurant_info'] = None
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Thank you for your message! We will get back to you soon.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

def contact_success(request):
    """View for contact success page"""
    try:
        restaurant_info = RestaurantInfo.objects.first()
    except RestaurantInfo.DoesNotExist:
        restaurant_info = None
    
    context = {
        'restaurant_info': restaurant_info,
    }
    return render(request, 'contact/contact_success.html', context)
