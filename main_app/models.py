from django.db import models
from django.urls import reverse

LISTENED = (
  ('F', 'A few songs'),
  ('A', 'The first half'),
  ('B', 'The second half'),
  ('W', 'The whole record')
)

# Create your models here.
class Record(models.Model):
  name = models.CharField(max_length=100)
  artist = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  release_year = models.IntegerField()
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("records_detail", kwargs={"record_id": self.id})

class Spun(models.Model):
  date = models.DateField('Last Spun')
  listened = models.CharField(
    max_length=1,
    choices=LISTENED,
    default=LISTENED[0][0]
  )
  
  record = models.ForeignKey(Record, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_listened_display()} on {self.date}"