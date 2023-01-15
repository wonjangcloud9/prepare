from django.shortcuts import render

# Create your views here.

from polls.models import Question, Answer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

def index(request):
    question_list = Question.objects.all()
    context = {'latest_question_list': question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    try:
        selected_answer = question.answer_set.get(id=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_answer.votes += 1
        selected_answer.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


class About(View):
    template_name = 'polls/about.html'