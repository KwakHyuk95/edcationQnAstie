from django.db import models

# Create your models here.
class MathQuestion(models.Model):
    subject = models.CharField(max_length=200)
    detail_subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class MathAnswer(models.Model):
    question = models.ForeignKey(MathQuestion, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
