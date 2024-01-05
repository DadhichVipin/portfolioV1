from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact_form, name='contact_form'),
]
