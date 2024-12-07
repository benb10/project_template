from django.db import models
from fastadmin import DjangoModelAdmin, register


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


@register(Question)
class QuestionAdmin(DjangoModelAdmin):
    pass
