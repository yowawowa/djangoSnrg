from django.urls import path
# from news.views import index, getCategory, toc, view_news, add_news
from news.views import HomeNews, NewsByCategory, toc, ViewNews, add_news

urlpatterns = [
    path('home', HomeNews.as_view(), name='Home'),
    path('', toc, name='Start'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>', ViewNews.as_view(), name='View_news'),
    path('news/add_news', add_news, name='Add_news'),
]
