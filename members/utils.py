from django.core.cache import cache

from .models import Member

MEMBER_COUNT_CACHE_KEY = "member_count"


def get_member_count():
    count = cache.get(MEMBER_COUNT_CACHE_KEY)
    if count is None:                                          # cache miss
        count = Member.objects.count()
        cache.set(MEMBER_COUNT_CACHE_KEY, count, timeout=60)   # keep it for 60 seconds
    return count
