from django.test import TestCase
from django.utils import timezone
from . models import Question
import datetime

# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_whit_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        # time = timezone.localtime(timezone.now()) + datetime.timedelta(days=30)
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        # 前面接你要測的方法，後面輸入預期的結果

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the old.
        """
        # time = timezone.localtime(timezone.now()) - \
        #     datetime.timedelta(days=1, seconds=1)
        # old_question = Question(pub_date=time)
        # self.assertIs(old_question.was_published_recently(), False)
        time = timezone.now() - \
            datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the old.
        """
        # time = timezone.localtime(timezone.now()) - \
        #     datetime.timedelta(hours=23, minutes=59, seconds=59)
        # recent_question = Question(pub_date=time)
        time = timezone.now() - \
            datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
