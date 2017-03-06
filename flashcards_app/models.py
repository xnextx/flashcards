from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=1000, verbose_name="group name")


class Content(models.Model):
    owner = models.ForeignKey(User)
    datetime = models.DateTimeField(verbose_name="date and time added Answer")
    image = models.ImageField(verbose_name="image to answer", blank=True)
    group = models.ManyToManyField(Group, related_name="groupquestion", verbose_name="group of question", blank=True)
    content_1 = models.TextField(max_length=10000, verbose_name="content 1")
    sentence_1 = models.TextField(max_length=10000, verbose_name="sentences to content 1", blank=True)
    content_2 = models.TextField(max_length=10000, verbose_name="content 2")
    sentence_2 = models.TextField(max_length=10000, verbose_name="sentences to content 2", blank=True)

    def __str__(self):
        return self.content_1 + " - " + self.content_2


class Progress(models.Model):
    owner = models.ForeignKey(User)
    question = models.ForeignKey(Content)
    know = models.ManyToManyField(Content, related_name="knownquestions", blank=True)
    dont_know = models.ManyToManyField(Content, related_name="unknownquestions", blank=True)
    to_repeat = models.ManyToManyField(Content, related_name="questionstorepeat", blank=True)
