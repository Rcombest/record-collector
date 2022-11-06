from django.shortcuts import render
from django.http import HttpResponse

class Record:
  def __init__(self, name, artist, description, release_year):
    self.name = name
    self.artist = artist
    self.description = description
    self.release_year = release_year

records = [
  Record("God's Country", "Chat Pile", "Bone-crushing, homegrown American nihilism", 2022),
  Record("The Expanding Universe", "Laurie Spiegel", "Beautiful synth soundscapes to soothe the soul", 1980),
  Record("The Epic", "Kamasi Washington", "Fantastic three hour modern jazz odyssey", 2015)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Henlo</h1>')

def about(request):
  return render(request, 'about.html')

def records_index(request):
  return render(request, 'records/index.html', { 'records': records })