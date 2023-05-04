from django.shortcuts import render
from .models import News


# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Newsletter'
    }
    return render(request, 'index.html', context)
