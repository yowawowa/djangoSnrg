from django.shortcuts import render
from .models import Answer, Human


# Create your views here.
def answer(request):
    answers = Answer.objects.all()
    context = {
        'answer': answers,
    }
    return render(request, 'answers/answer.html', context=context)


def human(request):
    human = Human.objects.all()
    context = {'human': human, }
    return render(request, 'answers/human.html', context=context)
