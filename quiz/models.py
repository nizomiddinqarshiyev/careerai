from django.db import models

from users.models import CustomUser


# from rest_framework.authtoken.admin import User
# from django.contrib.auth.models import User

# Create your models here.


class Careers(models.Model):
    name = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.name
    

class RoadMaps(models.Model):
    careers_id = models.ForeignKey(Careers, on_delete=models.CASCADE, related_name='roadmaps_set')
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Body(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    roadmaps_id = models.ForeignKey(RoadMaps, on_delete=models.CASCADE, related_name='body_set')

    def __str__(self):  
        return self.name
    

class Question(models.Model):
    question = models.CharField(max_length=200)
    test_id = models.ForeignKey('Test', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Options(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    A_B_option = models.CharField(max_length=100)
    
    def __str__(self):
        return self.A_B_option


class Type(models.Model):   
    
    name = models.CharField(max_length=200)
    number_of_tests = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return self.name


class Test(models.Model):
    careers_id = models.ForeignKey(Careers, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TestItem(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)


class Answer(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    test_item_id = models.ForeignKey(TestItem, on_delete=models.CASCADE)
    score = models.IntegerField()

class TestResult(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()

class Course(models.Model):
    name = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(max_length=100)
    file_url = models.FileField(max_length=100, upload_to='lessons/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

class DoneCourse(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    end_career = models.BooleanField(default=False)