from django.db import models
import os
import uuid

# Create your models here.
def std_photo_upload_path(instance, filename):     #instance--db, filename--imagename
    ext=filename.split('.')[-1]     #filename=img.png ---> split('.') --> [img, png]  -- [-1] -->png
    filename=f"{uuid.uuid4()} . {ext}"
    return os.path.join('student_photos', filename)

class Student(models.Model):
    name=models.CharField(max_length=100)
    student_class=models.CharField(max_length=50)
    section=models.CharField(max_length=10)
    student_id=models.CharField(max_length=20, unique=True)
    photo=models.ImageField(upload_to=std_photo_upload_path)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

