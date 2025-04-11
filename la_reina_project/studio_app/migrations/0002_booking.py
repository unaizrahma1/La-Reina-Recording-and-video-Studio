# Generated by Django 5.1.5 on 2025-04-11 07:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField()),
                ('session_type', models.CharField(choices=[('Recording', 'Recording'), ('Mixing', 'Mixing'), ('Mastering', 'Mastering'), ('Practice', 'Practice'), ('Other', 'Other')], max_length=50)),
                ('duration', models.DurationField(help_text='Format: hh:mm:ss')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='studio_app.artist')),
            ],
        ),
    ]
