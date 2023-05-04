from django.urls import path
from news.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
