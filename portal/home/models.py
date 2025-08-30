from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Roll_no = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(unique=True)
    Course = models.CharField(max_length=50)
    Year = models.IntegerField()

    def __str__(self):
        return f"{self.Name} ({self.Roll_no})"

