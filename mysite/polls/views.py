from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list' : latest_question_list})
 
def detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, "polls/detail.html", {'question' : question})

def result(request, question_id):
   response  = "you are looking at question %s."
   return HttpResponse(response % question_id)

def vote(request, question_id):
   response  = "youre voting on ques %s "
   return HttpResponse(response % question_id)
 