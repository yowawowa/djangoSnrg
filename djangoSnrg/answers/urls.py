from django.urls import path
from answers.views import answer, human, getProfession, view_human, add_human

urlpatterns = [
    path('', answer, name='Answers'),
    path('humans', human, name='Human'),
    path('profession/<int:profession_id>', getProfession, name='Profession'),
    path('human/<int:human_id>', view_human, name='View_human'),
    path('human/add_human', add_human, name='Add_human'),
]
