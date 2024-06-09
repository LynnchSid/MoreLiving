from Notification.models import  Notification
from Booking.models import Booking
from django.utils import timezone
from datetime import timedelta

def send_booking_confirmation(user, booking):
    message = f"Your booking at {booking.restaurant.name} on {booking.bookingDate} at {booking.bookingTime} has been confirmed."
    Notification.objects.create(user=user, notification_type='booking_confirmation', message=message)

def send_booking_reminder():
    now = timezone.now()
    reminder_time = now + timedelta(hours=1)  # 1 hour before the booking
    bookings = Booking.objects.filter(bookingDate=reminder_time.date(), bookingTime__hour=reminder_time.hour, bookingTime__minute=reminder_time.minute)
    for booking in bookings:
        message = f"Reminder: Your booking at {booking.restaurant.name} is in one hour."
        Notification.objects.create(user=booking.user, notification_type='booking_reminder', message=message)

def send_review_request(user, booking):
    message = f"We hope you enjoyed your visit to {booking.restaurant.name}. Please leave a review."
    Notification.objects.create(user=user, notification_type='review_request', message=message)

def send_special_offer(user, offer):
    message = f"Special offer: {offer.description}"
    Notification.objects.create(user=user, notification_type='special_offer', message=message)
