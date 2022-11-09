from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('records/', views.records_index, name='records_index'),
  path('records/<int:record_id>/', views.records_detail, name='records_detail'),
  path('records/create/', views.RecordCreate.as_view(), name='records_create'),
  path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
  path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),
  path('records/<int:record_id>/add_spun/', views.add_spun, name='add_spun'),
  path('records/<int:record_id>/assoc_song/<int:song_id>/', views.assoc_song, name='assoc_song'),
  path('songs/create/', views.SongCreate.as_view(), name="songs_create"),
  path('songs/<int:pk>/', views.SongDetail.as_view(), name='songs_detail'),
  path('songs/', views.SongList.as_view(), name='songs_index'),
  path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
  path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
]