# home/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def students(request):
    return render(request, 'home/students.html')

def teachers(request):
    return render(request, 'home/teachers.html')

def marks(request):
    return render(request, 'home/marks.html')

def attendance(request):
    return render(request, 'home/attendance.html')
