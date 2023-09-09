from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Title should not start with numbers')
        return title

    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'}),
        }

        # title = forms.CharField(max_length=150, label='Title', widget=forms.TextInput(attrs={
        #     'class': 'form-control',
        # }))
        # content = forms.CharField(label='Content', required=False, widget=forms.Textarea(attrs={
        #     'class': 'form-control',
        #     'rows': 5,
        # }))
        # is_published = forms.BooleanField(label='Published', initial=True)
        # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='Select a category', widget=forms.Select(attrs={
        #     'class': 'form-control',
        # }))
