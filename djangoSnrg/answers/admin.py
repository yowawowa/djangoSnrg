from django.contrib import admin
from .models import Answer, Human, Profession


# Register your models here.
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'question', 'answer')
    list_display_links = ('lesson', 'answer')
    search_fields = ('lesson',)


class HumansAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profession', 'height', 'address')
    list_editable = ('profession', 'address')
    list_display_links = ('id', 'name',)


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Answer, AnswersAdmin)
admin.site.register(Human, HumansAdmin)
admin.site.register(Profession, ProfessionAdmin)
