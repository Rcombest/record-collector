from django.db import models

# Create your models here.
class Record(models.Model):
  name = models.CharField(max_length=100)
  artist = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  release_year = models.IntegerField()
  
  def __str__(self):
    return self.name