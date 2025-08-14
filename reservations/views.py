from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Reservation
from .forms import ReservationForm
from core.models import RestaurantInfo

class ReservationCreateView(CreateView):
    """View for creating new reservations"""
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/reservation_form.html'
    success_url = reverse_lazy('reservation_success')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['restaurant_info'] = RestaurantInfo.objects.first()
        except RestaurantInfo.DoesNotExist:
            context['restaurant_info'] = None
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Reservation submitted successfully! We will confirm your booking shortly.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

def reservation_success(request):
    """View for reservation success page"""
    try:
        restaurant_info = RestaurantInfo.objects.first()
    except RestaurantInfo.DoesNotExist:
        restaurant_info = None
    
    context = {
        'restaurant_info': restaurant_info,
    }
    return render(request, 'reservations/reservation_success.html', context)
