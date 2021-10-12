from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Krquestion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_krquestion')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_krquestion')  # 추천인

    def __str__(self):
        return self.subject

class Kranswer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_kranswer')
    question = models.ForeignKey(Krquestion, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_kranswer')  # 추천인