from django.db import models

# Create your models here.

class QuizModel(models.Model):
    question = models.CharField('Question',max_length=250, null=True)
    option1 = models.CharField('Option 1',max_length=250, null=True)
    option2 = models.CharField('Option 2',max_length=250, null=True)
    option3 = models.CharField('Option 3',max_length=250, null=True)
    option4 = models.CharField('Option 4',max_length=250, null=True)
    answer = models.CharField('Answer',max_length=250, null=True)

    def __str__(self):
        return self.question
