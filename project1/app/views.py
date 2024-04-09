from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View, TemplateView, FormView
# Create your views here.


def Insert_School(request):
    ESFO = SchoolForm()
    d = {'ESFO':ESFO}
    if request.method == 'POST':
        SFDO = SchoolForm(request.POST)
        SFDO.save()
        return HttpResponse('School Created Successfully')
    return render(request, 'Insert_School_byfbv.html', d)

class Insert_School_bycbv(View):
    def get(self, request):
        ESFO = SchoolForm()
        d = {'ESFO':ESFO}
        return render(request, 'Insert_School_byfbv.html', d)
    
    def post(self, request):
        SFDO = SchoolForm(request.POST)
        SFDO.save()
        return HttpResponse('School Created Successfully')
    
class Template(TemplateView):
    template_name='template.html'
    

class Studentform(FormView):
    model=Student
    template_name='Studentform.html'
    
