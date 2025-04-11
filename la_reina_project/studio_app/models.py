from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    bio = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='artist_images/')

    def __str__(self):
        return self.name