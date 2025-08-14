from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    """Model for contact form submissions"""
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('reservation', 'Reservation Question'),
        ('feedback', 'Feedback'),
        ('complaint', 'Complaint'),
        ('partnership', 'Partnership'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('closed', 'Closed'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.status})"
