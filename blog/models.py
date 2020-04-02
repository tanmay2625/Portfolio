from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=30)
    pub_date=models.DateField()
    body=models.TextField(max_length=10000)
    image=models.ImageField(upload_to='images/')
