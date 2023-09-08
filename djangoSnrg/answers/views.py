from django.shortcuts import render
from .models import Answer, Human, Profession


# Create your views here.
def answer(request):
    answers = Answer.objects.all()
    context = {
        'answer': answers,
    }
    return render(request, 'answers/answer.html', context=context)


def human(request):
    humans = Human.objects.all()
    professions = Profession.objects.all()
    context = {'human': humans,
               'professions': professions}
    return render(request, 'answers/human.html', context=context)


def getProfession(request, profession_id):
    humans = Human.objects.filter(profession_id=profession_id)
    professions = Profession.objects.all()
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'humans': humans,
        'profession': profession,
    }
    return render(request, 'answers/profession.html', context=context)
