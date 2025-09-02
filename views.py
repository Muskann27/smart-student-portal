# home/views.py

from django.shortcuts import render
from .models import Student, Teacher, Marks, Attendance  # import all models


def index(request):
    return render(request, 'home/index.html')


def students(request):
    student_list = Student.objects.all()
    return render(request, "home/students.html", {"students": student_list})


def teachers(request):
    teacher_list = Teacher.objects.all()  # fetch all teachers from DB
    return render(request, "home/teachers.html", {"teachers": teacher_list})



def marks(request):
    marks_list = Marks.objects.all()  # fetch all marks
    return render(request, "home/marks.html", {"marks": marks_list})

def attendance(request):
    attendance_list = Attendance.objects.all()  # fetch all attendance records
    return render(request, "home/attendance.html", {"attendance": attendance_list})