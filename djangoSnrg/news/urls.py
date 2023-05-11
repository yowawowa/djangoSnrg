from django.urls import path
from news.views import index, getCategory

urlpatterns = [
    path('', index, name='Home'),
    path('category/<int:category_id>', getCategory, name='Category')
]
