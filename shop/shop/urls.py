# myproject/urls.py
from django.contrib import admin
from django.urls import path
from foto.views import ml
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", ml, name="index"),  # Sadece ml.html çalışacak
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
