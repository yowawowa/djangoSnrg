from django.urls import path
from answers.views import answer, human, getProfession

urlpatterns = [
    path('', answer, name='Answers'),
    path('humans', human, name='Human'),
    path('profession/<int:profession_id>', getProfession, name='Profession'),
]
