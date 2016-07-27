from django.conf import settings


def map_key():
    return {
        "googlemap_key": settings.MAP_KEY,
    }
