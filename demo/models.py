from django.db import models

# Create your models here.
class Book(models.Model):
    # field: 
    # unique: title would be unique in db
    # choice: limit the title you can choose 
    # null, blank ,, 

    title = models.CharField(max_length=36, unique=True)
    description = models.TextField(max_length=256, blank = True)
    price = models.DecimalField(default=0.0)
    published = models.DateField(auto_now=True, auto_now_add=True)
