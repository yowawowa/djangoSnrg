from django import forms
from .models import Profession, Human
import re
from django.core.exceptions import ValidationError


class HumanForm(forms.ModelForm):

    def clean_title(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('Name should not start with numbers')
        return name

    class Meta:
        model = Human
        fields = ['name', 'height', 'address', 'profession']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'height': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'profession': forms.Select(attrs={
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
