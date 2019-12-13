from django.db import models

# Create your models here.
class user_data(models.Model):
    first_name=models.CharField(max_length=264)
    last_name=models.CharField(max_length=264)
    email=models.EmailField(max_length=264)
    def __str__(self):
        return self.first_name+" "+self.last_name+" "+self.email
