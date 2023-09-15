from django import forms
from .models import Human
import re
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class HumanForm(forms.ModelForm):
    captcha = CaptchaField()

    def clean_title(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('Name should not start with numbers')
        return name

    class Meta:
        model = Human
        fields = ['name', 'height', 'address', 'profession', 'description']
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
            'description': forms.Textarea(attrs={
                'class': 'form-control'}),
        }