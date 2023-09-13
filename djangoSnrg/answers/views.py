from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .models import Answer, Human, Profession
from .forms import HumanForm
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator


def tester(request):
    objects = Human.objects.all()
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'answers/tester.html', {'page_obj': page_objects, })


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
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of humans'
        return context

    def get_queryset(self):
        return Human.objects.all().select_related('profession')


class HumansByProfession(ListView):
    model = Human
    template_name = 'answers/profession.html'
    context_object_name = 'professions'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Profession.objects.get(pk=self.kwargs['profession_id'])
        return context

    def get_queryset(self):
        return Human.objects.filter(profession_id=self.kwargs['profession_id']).select_related('profession')


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


class AddHuman(CreateView, LoginRequiredMixin):
    form_class = HumanForm
    template_name = 'answers/add_human.html'
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ('Add human')
        return context
