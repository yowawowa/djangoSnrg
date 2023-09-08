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
    humans = Human.objects.all()
    context = {'human': humans, }
    return render(request, 'answers/human.html', context=context)
