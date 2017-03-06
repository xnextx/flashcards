from django.shortcuts import render
from flashcards_app.models import *
# import os
# from .models import Content
# import datetime
# Create your views here.

def download_questions(request):
    questions = []
    for x in Content.objects.filter(owner=request.user):
        questions.append({'question': x.content_1, 'answer': x.content_2})
    return questions

def main(request):
    # target1 = open(os.path.dirname(__file__) + '/words/words_en.txt', 'r').read().split("\n")
    # target2 = open(os.path.dirname(__file__) + '/words/words_pl.txt', 'r').read().split("\n")
    #
    #
    # for id, x in enumerate(target1):
    #     content_ob = Content()
    #     content_ob.owner = request.user
    #     content_ob.datetime = datetime.datetime.today()
    #     content_ob.content_1 = target2[id]
    #     content_ob.content_2 = target1[id]
    #     content_ob.save()
    #     print(x)

    return render(request, 'main.html', {
        'questions_all': download_questions(request)
    })