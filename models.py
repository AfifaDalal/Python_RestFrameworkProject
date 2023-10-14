from django.db import models

# Create your models here.
class StudentModel(models.Model):
	sid=models.IntegerField()
	sname=models.CharField(max_length=20)
	scourse=models.CharField(max_length=10)

	def __str__(self):
		return self.sname