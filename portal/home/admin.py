from django.contrib import admin
from .models import Student

admin.site.register(Student)

# teacher
from .models import Teacher

admin.site.register(Teacher)


# marks

from .models import Marks

admin.site.register(Marks)


# ATTENDANCE
from .models import Attendance

admin.site.register(Attendance)
