from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta

class Reservation(models.Model):
    """Model for table reservations"""
    TIME_CHOICES = [
        ('11:00', '11:00 AM'),
        ('11:30', '11:30 AM'),
        ('12:00', '12:00 PM'),
        ('12:30', '12:30 PM'),
        ('13:00', '1:00 PM'),
        ('13:30', '1:30 PM'),
        ('14:00', '2:00 PM'),
        ('14:30', '2:30 PM'),
        ('17:00', '5:00 PM'),
        ('17:30', '5:30 PM'),
        ('18:00', '6:00 PM'),
        ('18:30', '6:30 PM'),
        ('19:00', '7:00 PM'),
        ('19:30', '7:30 PM'),
        ('20:00', '8:00 PM'),
        ('20:30', '8:30 PM'),
        ('21:00', '9:00 PM'),
        ('21:30', '9:30 PM'),
        ('22:00', '10:00 PM'),
    ]

    PARTY_SIZE_CHOICES = [
        (1, '1 person'),
        (2, '2 people'),
        (3, '3 people'),
        (4, '4 people'),
        (5, '5 people'),
        (6, '6 people'),
        (7, '7 people'),
        (8, '8 people'),
        (9, '9 people'),
        (10, '10 people'),
        (11, '11+ people'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    party_size = models.IntegerField(choices=PARTY_SIZE_CHOICES)
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-time']
        unique_together = ['date', 'time', 'name', 'email']

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time} ({self.party_size} people)"

    def clean(self):
        from django.core.exceptions import ValidationError
        # Check if reservation is not in the past
        if self.date < datetime.now().date():
            raise ValidationError("Cannot make reservations for past dates.")
        
        # Check if reservation is not too far in the future (e.g., 3 months)
        if self.date > datetime.now().date() + timedelta(days=90):
            raise ValidationError("Cannot make reservations more than 3 months in advance.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
