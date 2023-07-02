from django.db import models
from django.urls import reverse
class tasks(models.Model):
    task=models.CharField(max_length=255)
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    published_date=models.DateField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    def get_api_url(self):
        return reverse('blog:api-v1:my_practic',kwargs={"pk":self.pk})

