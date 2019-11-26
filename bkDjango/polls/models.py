from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now=True)
    pub_date = models.DateTimeField('date published')
    modify_date = models.DateTimeField('date modified',null=True,)
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.localtime(timezone.now())
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 
        # 只介於昨天與今天之間

        # if self.pub_date <= timezone.localtime(timezone.now()):
        #     return self.pub_date >= timezone.localtime(timezone.now()) - datetime.timedelta(days=1)
        #     # 只要時間是在我昨天之後，就是最近發生
        # else:
        #     return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text