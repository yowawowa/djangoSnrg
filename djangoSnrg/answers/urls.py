from django.urls import path
from answers.views import answer, human

urlpatterns = [
    path('', answer, name='Answers'),
    path('human', human, name='Human'),
]
