# home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),              # Homepage
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('marks/', views.marks, name='marks'),
    path('attendance/', views.attendance, name='attendance'),
]

