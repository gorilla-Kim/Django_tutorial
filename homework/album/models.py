from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length = 225)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:20]