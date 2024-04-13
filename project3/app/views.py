from django.shortcuts import render
from django.http import HttpResponse
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


class DisplaySchool(DetailView):
    model=School
    context_object_name = 'school'


class UpdateSchool(UpdateView):
    model=School
    fields='__all__'
    success_url=reverse_lazy('Schoollist')

def func(request):
    SO = School.objects.all()
    d = {'SO':SO}
    return render(request, 'app/schools.html', d)

def demo(request, name):
    SO = School.objects.get(sname=name)
    d = {'SO':SO}
    return render(request, 'app/dynamic.html', d)
    # return HttpResponse(f"<h1>Hello {name}</h1>")