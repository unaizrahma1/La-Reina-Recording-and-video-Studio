from django.test import TestCase, Client
from django.urls import reverse
from .models import Artist, Booking
from datetime import datetime, timedelta, time

class ArtistModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            name="Test Artist",
            genre="Hip Hop",
            bio="Just a test artist",
            contact="1234567890",
            email="test@example.com",
            image="artist_images/test.jpg"
        )

    def test_create_artist(self):
        self.assertEqual(Artist.objects.count(), 1)
        self.assertEqual(self.artist.name, "Test Artist")

    def test_update_artist(self):
        self.artist.name = "Updated Name"
        self.artist.save()
        self.assertEqual(Artist.objects.get(id=self.artist.id).name, "Updated Name")

    def test_delete_artist(self):
        self.artist.delete()
        self.assertEqual(Artist.objects.count(), 0)

class BookingModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            name="Booking Artist",
            genre="Jazz",
            bio="Jazz artist",
            contact="0987654321",
            email="jazz@example.com",
            image="artist_images/jazz.jpg"
        )
        self.booking = Booking.objects.create(
            artist=self.artist,
            date="2024-04-15",
            time="12:00",
            session_type="Recording",
            duration=timedelta(hours=2)
        )

    def test_create_booking(self):
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(self.booking.duration, timedelta(hours=2))

    def test_update_booking(self):
        self.booking.session_type = "Mixing"
        self.booking.save()
        self.assertEqual(Booking.objects.get(id=self.booking.id).session_type, "Mixing")

    def test_delete_booking(self):
        self.booking.delete()
        self.assertEqual(Booking.objects.count(), 0)

class IntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = Artist.objects.create(
            name="Integration Artist",
            genre="Rock",
            bio="Performs rock",
            contact="1112223333",
            email="rock@example.com",
            image="artist_images/rock.jpg"
        )

    def test_booking_submission(self):
        response = self.client.post(reverse('add_booking'), {
            'artist': self.artist.id,
            'date': '2025-04-20',
            'time': '14:00',
            'session_type': 'Practice',
            'duration': '01:30:00'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Booking added successfully!")
        self.assertEqual(Booking.objects.count(), 1)
