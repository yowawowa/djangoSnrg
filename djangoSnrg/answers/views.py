from django.shortcuts import render, get_object_or_404, redirect
from .models import Answer, Human, Profession
from .forms import HumanForm


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


def view_human(request, human_id):
    human_item = get_object_or_404(Human, pk=human_id)
    context = {
        'human_item': human_item,
    }
    return render(request, 'answers/view_human.html', context=context)


def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(human)
    else:
        form = HumanForm()
    return render(request, 'answers/add_human.html', {'form': form})
