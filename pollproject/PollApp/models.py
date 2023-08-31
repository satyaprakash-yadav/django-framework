from django.db import models

# Create your models here.

class PollRecord(models.Model):

    creation = models.DateTimeField(auto_now_add=True)
    
    question = models.CharField(max_length=100)

    option1 = models.CharField(max_length=50)

    option2 = models.CharField(max_length=50)

    option3 = models.CharField(max_length=50)

    option4 = models.CharField(max_length=50)

    vote_one = models.IntegerField(default=0)

    vote_two = models.IntegerField(default=0)

    vote_three = models.IntegerField(default=0)

    vote_four = models.IntegerField(default=0)

    def clean(self):
        self.question = self.question.capitalize()

    def __str__(self):
        return self.question


