from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation
from datetime import datetime, timedelta

class ReservationForm(forms.ModelForm):
    """Form for making table reservations"""
    
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'party_size', 'special_requests']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'min': datetime.now().strftime('%Y-%m-%d'),
                'max': (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')
            }),
            'time': forms.Select(attrs={
                'class': 'form-select'
            }),
            'party_size': forms.Select(attrs={
                'class': 'form-select'
            }),
            'special_requests': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Any special requests or dietary restrictions?'
            }),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date:
            if date < datetime.now().date():
                raise ValidationError("Cannot make reservations for past dates.")
            if date > datetime.now().date() + timedelta(days=90):
                raise ValidationError("Cannot make reservations more than 3 months in advance.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        
        if date and time:
            # Check if it's a valid reservation time (not during closed hours)
            current_time = datetime.now().time()
            reservation_time = datetime.strptime(time, '%H:%M').time()
            
            # If making reservation for today, check if time has passed
            if date == datetime.now().date() and reservation_time < current_time:
                raise ValidationError("Cannot make reservations for times that have already passed.")
        
        return cleaned_data
