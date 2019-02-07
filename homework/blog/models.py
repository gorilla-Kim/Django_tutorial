from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 125)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length = 15)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.title[:20]