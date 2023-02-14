import datetime
import time
from django.db import models
from time import mktime

from django.utils import timezone
from django.utils.timezone import datetime, timedelta
from datetime import datetime

class Question(models.Model):
   question_text = models.fieldName= models.CharField(max_length = 150)
   pub_date = models.fieldName = models.DateTimeField(auto_now=False, auto_now_add=False)
   
   def __str__(self):
      return self.question_text

   def was_published_recently(self):
      now = timezone.now()
      return now - datetime.timedelta(days=1) <= self.pub_date <= now
   


class Choice(models.Model):
   question = models.fieldName = models.ForeignKey(Question, on_delete=models.CASCADE)
   choice_text = models.fieldName = models.CharField(max_length = 150)
   votes = models.fieldName = models.IntegerField()

   def __str__(self):
      return self.choice_text
   
# Create your models here.
