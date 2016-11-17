from django.shortcuts import render, HttpResponse, redirect
from .models import Courses

# Create your views here.

def index(request):
    context={
    'courses': Courses.objects.all()
    }
    print Courses.objects.all()
    return render(request, 'courses/index.html',context)

def add(request):
    Courses.objects.create(course_name=request.POST['name'],course_description=request.POST['description'])
    return redirect('/')

def delete(request,id):
    course=Courses.objects.get(id=id)
    context={
    'course':course
    }
    return render(request, 'courses/delete.html',context)

def yesdelete(request,id):
    Courses.objects.filter(id=id).delete()
    return redirect('/')
