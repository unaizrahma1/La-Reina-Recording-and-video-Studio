from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    bio = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='artist_images/')

    def __str__(self):
        return self.name

class Booking(models.Model):
    SESSION_CHOICES = [
        ('Recording', 'Recording'),
        ('Mixing', 'Mixing'),
        ('Mastering', 'Mastering'),
        ('Practice', 'Practice'),
        ('Other', 'Other'),
    ]

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField(default=timezone.now)
    time = models.TimeField()
    session_type = models.CharField(max_length=50, choices=SESSION_CHOICES)
    duration = models.DurationField(help_text="Format: hh:mm:ss")

    def __str__(self):
        return f"{self.artist.name} - {self.session_type} on {self.date} at {self.time}"