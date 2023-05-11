from django.contrib import admin
from .models import Answer, Human

# Register your models here.
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'question', 'answer')
    list_display_links = ('lesson', 'answer')
    search_fields = ('lesson',)





admin.site.register(Answer, AnswersAdmin)
admin.site.register(Human)