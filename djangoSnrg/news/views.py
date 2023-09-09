from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm


# Create your views here.
def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Newsletter',
    }
    return render(request, 'news/index.html', context=context)


def toc(request):
    return render(request, 'news/toc.html', context=None)


def getCategory(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context=context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request, 'news/view_news.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
