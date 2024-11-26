from django.urls import path
from . import views

urlpatterns = [
    path('', views.court_time, name='court_timer'),
]
