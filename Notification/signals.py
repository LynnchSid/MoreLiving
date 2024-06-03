from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from Booking.models import Booking
from Notification.notifications import send_booking_confirmation, send_review_request
from Notification.models import Notification

@receiver(post_save, sender=Booking)
def booking_created(sender, instance, created, **kwargs):
    if created:
        send_booking_confirmation(instance.user, instance)
        # Schedule a reminder one hour before the booking
        # This would typically be done with a task scheduler like Celery

@receiver(post_save, sender=Booking)
def booking_completed(sender, instance, **kwargs):
    # Assuming there's a field or a status to check if booking is completed
    if instance.is_completed:
        send_review_request(instance.user, instance)

# Repeat similarly for other models and events

@receiver(post_save, sender=Notification)
def notification_created(sender, instance, created, **kwargs):
    if created:
        send_review_request(instance.user, instance)

@receiver(post_save, sender=Notification)
def notification_deleted(sender, instance, **kwargs):
    if instance.notification_type == 'review_request':
        send_booking_confirmation(instance.user, instance)

@receiver(post_save, sender=Notification)
def notification_updated(sender, instance, **kwargs):
    if instance.notification_type == 'review_request':
        send_booking_confirmation(instance.user, instance)