from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Answer, Human, Profession



class HumanAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Human
        fields ='__all__'

# Register your models here.
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'question', 'answer')
    list_display_links = ('lesson', 'answer')
    search_fields = ('lesson',)


class HumansAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_photo', 'profession', 'height', 'address','description')
    list_editable = ('profession', 'address')
    list_display_links = ('id', 'name',)
    fields = ('name', 'height', 'photo', 'get_photo', 'profession', 'address','description')
    readonly_fields = ('get_photo',)
    form = HumanAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'no photo'

        get_photo_description = 'miniature'


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Answer, AnswersAdmin)
admin.site.register(Human, HumansAdmin)
admin.site.register(Profession, ProfessionAdmin)
