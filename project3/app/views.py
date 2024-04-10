from django.shortcuts import render
from django.views.generic import *
from app.models import *
from django.urls import reverse_lazy
# Create your views here.

class InsertSchool(CreateView):
    model = School
    fields = '__all__'
    success_url = reverse_lazy('InsertSchool')

class Schoollist(ListView):
    model=School
    context_object_name = 'schools'


