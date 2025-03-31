from django.db import models

# Create your models here.
# myapp/models.py
# myapp/models.py
from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"

class sliderImage(models.Model):
    foto = models.ImageField(upload_to="sliderImage/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"foto {self.id}"

