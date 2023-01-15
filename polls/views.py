from django.shortcuts import render

# Create your views here.

from polls.models import Question, Answer

def index(request):
    question_list = Question.objects.all()
    context = {'latest_question_list': question_list}
    return render(request, 'polls/index.html', context)