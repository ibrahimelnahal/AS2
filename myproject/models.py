from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email = models.EmailField()
    #courses = models.ManyToManyField(Course)


    def __unicode__(self):
        return self.firstname
        return self.lastname



class Teacher(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    office=models.IntegerField(default=4)
    email = models.EmailField()
    phone=models.IntegerField()

    def __unicode__(self):
        return self.firstname
        return self.lastname



class Course(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=6)
    time=models.TimeField()
    classroom=models.CharField(max_length=6)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher)

    def __unicode__(self):
        return self.name

