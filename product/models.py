from django.db import models

class Product(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    weight=models.CharField(max_length=14)
    price=models.CharField(max_length=14)
  
    timeStamp=models.DateTimeField(blank=True)
   

    def __str__(self):
        return self.name + "  " + self.price

