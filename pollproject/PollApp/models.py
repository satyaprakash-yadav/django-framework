from django.db import models

# Create your models here.

class PollRecord(models.Model):

    creation = models.DateTimeField(auto_now_add=True)
    
    question = models.CharField(max_length=100)

    option1 = models.CharField(max_length=50)

    option2 = models.CharField(max_length=50)

    option3 = models.CharField(max_length=50)

    option4 = models.CharField(max_length=50)

    def __str__(self):
        return self.question
    
class Vote(models.Model):
    question = models.ForeignKey(PollRecord, on_delete=models.CASCADE, related_name='choices')
    vote = models.IntegerField(default=0)



