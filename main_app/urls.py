from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('records/', views.records_index, name='records_index'),
  path('records/<int:record_id>/', views.records_detail, name='records_detail'),
  path('records/create/', views.RecordCreate.as_view(), name='records_create'),
]