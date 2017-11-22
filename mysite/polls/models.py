from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
	"""docstring for ClassName"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('data published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	"""docstring for Choice"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	Choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.Choice_text

		
		