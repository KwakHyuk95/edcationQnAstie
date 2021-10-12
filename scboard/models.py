from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Scquestion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_scquestion')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_scquestion')  # 추천인

    def __str__(self):
        return self.subject

class Scanswer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_scanswer')
    question = models.ForeignKey(Scquestion, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_scanswer')  # 추천인