from django.contrib import admin
from .models import Record, Spun, Song

# Register your models here.
admin.site.register(Record)
admin.site.register(Spun)
admin.site.register(Song)