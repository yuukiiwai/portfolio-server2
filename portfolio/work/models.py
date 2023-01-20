from django.db import models

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=32)
    url = models.URLField(max_length=256)
    slide = models.CharField(max_length=2048)
    def __str__(self) -> str:
        return self.title