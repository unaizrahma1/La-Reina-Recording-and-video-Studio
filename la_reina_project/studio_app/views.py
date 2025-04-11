from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
from .models import Artist, Booking 
from datetime import timedelta, datetime

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

# Update artist
def update_artist(request, id):
    artist = get_object_or_404(Artist, id=id)

    if request.method == 'POST':
        artist.name = request.POST.get('name')
        artist.genre = request.POST.get('genre')
        artist.bio = request.POST.get('bio')
        artist.contact = request.POST.get('contact')
        artist.email = request.POST.get('email')

        if 'image' in request.FILES:
            artist.image = request.FILES['image']

        artist.save()
        messages.success(request, 'Artist updated successfully!')
        return redirect('artist_list')

    return render(request, 'update_artist.html', {'artist': artist})

# Delete artist
def delete_artist(request, id):
    artist = get_object_or_404(Artist, id=id)
    artist.delete()
    messages.success(request, 'Artist deleted successfully!')
    return redirect('artist_list')

def add_booking(request):
    if request.method == 'POST':
        artist_id = request.POST.get('artist')
        date = request.POST.get('date')
        time = request.POST.get('time')
        session_type = request.POST.get('session_type')
        duration_str = request.POST.get('duration')

        try:
            # Parse duration string (format hh:mm:ss)
            (hours, minutes, seconds) = map(int, duration_str.split(':'))
            duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)

            artist = Artist.objects.get(id=artist_id)
            booking = Booking.objects.create(
                artist=artist,
                date=date,
                time=time,
                session_type=session_type,
                duration=duration
            )
            messages.success(request, "Booking added successfully!")
            return redirect('booking_list')  # You can change to a bookings list if needed
        except Artist.DoesNotExist:
            messages.error(request, "Selected artist does not exist.")
        except ValueError:
            messages.error(request, "Duration must be in hh:mm:ss format.")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

    artists = Artist.objects.all()
    return render(request, 'add_booking.html', {'artists': artists})

def booking_list(request):
    bookings = Booking.objects.select_related('artist').order_by('-date', '-time')
    return render(request, 'booking_list.html', {'bookings': bookings})

from datetime import timedelta

def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        booking.artist_id = request.POST.get('artist_id')
        booking.date = request.POST.get('date')
        booking.time = request.POST.get('time')
        booking.session_type = request.POST.get('session_type')

        # Convert string hours to timedelta
        duration_str = request.POST.get('duration')
        try:
            duration_hours = float(duration_str)
            booking.duration = timedelta(hours=duration_hours)
        except ValueError:
            messages.error(request, 'Invalid duration format.')
            return redirect('update_booking', booking_id=booking_id)

        booking.save()
        messages.success(request, 'Booking updated successfully.')
        return redirect('booking_list')

    artists = Artist.objects.all()
    try:
        duration_hours = booking.duration.total_seconds() / 3600
    except AttributeError:
        duration_hours = booking.duration

    return render(request, 'update_booking.html', {
        'booking': booking,
        'artists': artists,
        'duration_hours': duration_hours,
    })


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, 'Booking deleted successfully.')
    return redirect('booking_list')