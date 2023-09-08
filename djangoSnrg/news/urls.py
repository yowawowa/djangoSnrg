from django.urls import path
from news.views import index, getCategory, toc

urlpatterns = [
    path('home', index, name='Home'),
    path('', toc, name='Start'),
    path('category/<int:category_id>', getCategory, name='Category')
]
