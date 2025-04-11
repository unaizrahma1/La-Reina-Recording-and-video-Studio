from django.shortcuts import render, redirect
from .models import Artist

def index(request):
    artists = Artist.objects.all()
    return render(request, 'index.html', {'artists': artists})

def add_artist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        genre = request.POST.get('genre')
        bio = request.POST.get('bio')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        Artist.objects.create(
            name=name,
            genre=genre,
            bio=bio,
            contact=contact,
            email=email,
            image=image
        )
        return redirect('index')
    
    return render(request, 'add_artist.html')
    
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists})