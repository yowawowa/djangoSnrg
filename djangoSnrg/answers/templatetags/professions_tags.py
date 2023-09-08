from answers.models import Profession
from django import template

register = template.Library()


@register.simple_tag(name='get_list_professions')
def getProfessions():
    return Profession.objects.all()

@register.inclusion_tag('answers/list_professions.html')
def showProfessions(arg1='Professions', arg2='list'):
    professions = Profession.objects.all()
    return {
        'professions': professions, 'arg1': arg1, 'arg2': arg2,
    }
