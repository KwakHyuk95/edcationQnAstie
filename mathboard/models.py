from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Mathquestion(models.Model):
    subject = models.CharField(max_length=200)
    detail_subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Mathanswer(models.Model):
    question = models.ForeignKey(Mathquestion, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
