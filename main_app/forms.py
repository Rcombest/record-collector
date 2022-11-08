from django.forms import ModelForm
from .models import Spun

class SpunForm(ModelForm):
  class Meta:
    model = Spun
    fields = ['date', 'listened']