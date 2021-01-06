from django.db import models
from django.utils import timezone

class Post(models.Model):
    cover = models.ImageField(upload_to='images/',default='soso.jpg')
    img1 = models.ImageField(upload_to='images/',default='soso.jpg')
    img2 = models.ImageField(upload_to='images/',default='soso.jpg')
    
    car_name=models.CharField(max_length=100)
    price=models.IntegerField()
    content=models.TextField()
    data_posted=models.DateTimeField(default=timezone.now)

def __str__(self):
    return {self.car_name}