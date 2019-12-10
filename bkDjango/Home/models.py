from django.db import models

# Create your models here.


class Index(models.Model):
    title = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    content_one = models.TextField()
    content_two = models.TextField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.title


class Student(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(null=True)
    def __str__(self):
        return "Student_intro"

class StudentSkill(models.Model):
    skill = models.CharField(max_length=20)
    create_at = models.DateTimeField()
    def __str__(self):
        return self.skill

class Worker(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(null=True)
    def __str__(self):
        return "work_intro"

class WorkSkill(models.Model):
    skill = models.CharField(max_length=20)
    create_at = models.DateTimeField()
    def __str__(self):
        return self.skill



