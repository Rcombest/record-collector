from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Record, Song
from .forms import SpunForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def records_index(request):
  records = Record.objects.filter(user=request.user)
  return render(request, 'records/index.html', { 'records': records })

@login_required
def records_detail(request, record_id):
  record = Record.objects.get(id=record_id)
  songs_record_doesnt_have = Song.objects.exclude(id__in = record.songs.all().values_list('id'))
  spun_form = SpunForm()
  return render(request, 'records/detail.html', { 
    'record': record, 
    'spun_form': spun_form,
    'songs': songs_record_doesnt_have
  })

class RecordCreate(CreateView):
  model = Record
  fields = ['name', 'artist', 'description', 'release_year']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RecordUpdate(UpdateView):
  model = Record
  fields = ['name', 'artist', 'description', 'release_year']

class RecordDelete(DeleteView):
  model = Record
  success_url = '/records/'

@login_required
def add_spun(request, record_id):
  form = SpunForm(request.POST)
  if form.is_valid():
    new_spun = form.save(commit=False)
    new_spun.record_id = record_id
    new_spun.save()
  return redirect('records_detail', record_id=record_id)

class SongCreate(CreateView):
  model = Song
  fields = "__all__"

class SongList(ListView):
  model = Song

class SongDetail(DetailView):
  model = Song

class SongUpdate(UpdateView):
  model = Song
  fields = ['name', 'fav_lyrics']

class SongDelete(DeleteView):
  model = Song
  success_url = '/songs/'

@login_required
def assoc_song(request, record_id, song_id):
  Record.objects.get(id=record_id).songs.add(song_id)
  return redirect('records_detail', record_id=record_id)

def signup(request):
  error_message = ""
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('records_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)