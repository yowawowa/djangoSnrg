from django.urls import path
from news.views import index, getCategory, toc, view_news, add_news

urlpatterns = [
    path('home', index, name='Home'),
    path('', toc, name='Start'),
    path('category/<int:category_id>', getCategory, name='Category'),
    path('news/<int:news_id>', view_news, name='View_news'),
    path('news/add_news', add_news, name='Add_news'),
]
