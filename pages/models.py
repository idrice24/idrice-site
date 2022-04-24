from django.db import models

# Create your models here.
# general syntax
# class name_of_table(model.Model)

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models:DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete= models.CASCADE)
	choice_text = odels.CharField(max_length=200)
	votes = models.IntegerField(default=0)