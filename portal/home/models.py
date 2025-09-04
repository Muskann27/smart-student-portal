from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Roll_no = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(unique=True)
    Course = models.CharField(max_length=50)
    Year = models.IntegerField()

    def __str__(self):
        return f"{self.Name} ({self.Roll_no})"

# teacher

class Teacher(models.Model):
    Name = models.CharField(max_length=100)
    Employee_id = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(unique=True)
    Department = models.CharField(max_length=50)
    Subject = models.CharField(max_length=100, default="Unknown")  # ✅ added with default

    def __str__(self):
        return f"{self.Name} ({self.Employee_id})"


# MARKS
class Marks(models.Model):
    Student = models.ForeignKey("Student", on_delete=models.CASCADE)
    Subject = models.CharField(max_length=100)
    Marks_Obtained = models.IntegerField()
    Teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.Student.Name} - {self.Subject}: {self.Marks_Obtained}"

    class Meta:
        verbose_name_plural = "Marks"   # ✅ Fix plural spelling

    
# ATTENDANCE
class Attendance(models.Model):
    Student = models.ForeignKey("Student", on_delete=models.CASCADE)
    Subject = models.CharField(max_length=100)
    Date = models.DateField()
    Status = models.CharField(
        max_length=10,
        choices=[("Present", "Present"), ("Absent", "Absent")]
    )
    Teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True, blank=True)  # ✅ NEW

    def __str__(self):
        return f"{self.Student.Name} - {self.Subject} on {self.Date}: {self.Status}"


'''
ForeignKey(Student) → each attendance record belongs to a student.

Subject → subject name.

Date → date of the class.

Status → either Present or Absent.
'''
