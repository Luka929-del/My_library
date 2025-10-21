from django.urls import path
from . import views

urlpatterns = [
    path('', views.reader_form, name='reader_form'),
]
