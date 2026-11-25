from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ReadingLog


@receiver(post_save, sender=ReadingLog)
def log_new_reading(sender, instance, created, **kwargs):
    if created:
        print(f"New reading saved: {instance}")
