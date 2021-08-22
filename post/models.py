from django.db import models

# Create your models here.


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.CharField(max_length=255)
    text=models.CharField(max_length=14)
    
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.user + "  " + self.text

