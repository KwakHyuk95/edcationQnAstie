from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Mathquestion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_mathquestion')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_mathquestion')  # 추천인

    def __str__(self):
        return self.subject

class Mathanswer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_mathanswer')
    question = models.ForeignKey(Mathquestion, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_mathanswer')  # 추천인