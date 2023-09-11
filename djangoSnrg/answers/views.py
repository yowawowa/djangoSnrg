from django.shortcuts import render, get_object_or_404, redirect
from .models import Answer, Human, Profession
from .forms import HumanForm
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.

class AnswersList(ListView):
    model = Answer
    context_object_name = 'answer'
    template_name = 'answers/answer.html'
    extra_context = {
        'title': 'Answers',
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Answer page'
        return context

    def get_queryset(self):
        return Answer.objects.all()


class HumanList(ListView):
    model = Human
    context_object_name = 'human'
    template_name = 'answers/human.html'
    extra_context = {
        'title': 'Human'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of humans'
        return context

    def get_queryset(self):
        return Human.objects.all()


def getProfession(request, profession_id):
    humans = Human.objects.filter(profession_id=profession_id)
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'humans': humans,
        'profession': profession,
    }
    return render(request, 'answers/profession.html', context=context)

class HumansByProfession(ListView):
    model = Human
    template_name = 'answers/profession.html'
    context_object_name = 'professions'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Profession.objects.get(pk=self.kwargs['profession_id'])
        return context

    def get_queryset(self):
        return Human.objects.filter(profession_id=self.kwargs['profession_id'])

def view_human(request, human_id):
    human_item = get_object_or_404(Human, pk=human_id)
    context = {
        'human_item': human_item,
    }
    return render(request, 'answers/view_human.html', context=context)

class ViewHuman(DetailView):
    model = Human
    context_object_name = 'human_item'
    template_name = 'answers/view_human.html'

def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            human = form.save()
            return redirect(human)
    else:
        form = HumanForm()
    return render(request, 'answers/add_human.html', {'form': form})
