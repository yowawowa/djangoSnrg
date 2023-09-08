from django.urls import path
from answers.views import answer, human

urlpatterns = [
    path('', answer, name='Answers'),
    path('humans', human, name='Human'),
]
