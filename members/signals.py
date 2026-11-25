# members/signals.py
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Member, ReadingLog
from .utils import MEMBER_COUNT_CACHE_KEY


@receiver(post_save, sender=ReadingLog)
def log_new_reading(sender, instance, created, **kwargs):
    if created:
        print(f"New reading saved: {instance}")


@receiver([post_save, post_delete], sender=Member)
def clear_member_count_cache(sender, **kwargs):
    # Drop the cached count so the home page recomputes it on the next request.
    cache.delete(MEMBER_COUNT_CACHE_KEY)
