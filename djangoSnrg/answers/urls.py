from django.urls import path
from answers.views import HumanList, HumansByProfession, ViewHuman, add_human, AnswersList

urlpatterns = [
    path('', AnswersList.as_view(), name='Answers'),
    path('humans', HumanList.as_view(), name='Human'),
    path('profession/<int:profession_id>', HumansByProfession.as_view(), name='Profession'),
    path('human/<int:pk>', ViewHuman.as_view(), name='View_human'),
    path('human/add_human', add_human, name='Add_human'),
]
