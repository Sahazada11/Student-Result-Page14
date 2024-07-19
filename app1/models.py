from django.db import models

# Create your models here.
class Marks(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=20)
    subject1=models.IntegerField(max_length=20)
    subject2=models.IntegerField(max_length=20)
    subject3=models.IntegerField(max_length=20)
    subject4=models.IntegerField(max_length=20)

   