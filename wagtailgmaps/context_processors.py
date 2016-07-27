from django.conf import settings


def googlemap_key(request):
    return {
        "googlemap_key": settings.GOOGLEMAP_KEY,
    }
