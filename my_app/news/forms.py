from .models import articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class articlesForm(ModelForm):
    class Meta:
        model = articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'name'
            }),
            "anons": TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'anons'
            }),
            "date": DateTimeInput(attrs = {
                'class': 'form-control',
                'placeholder': 'date'
            }),
            "full_text": Textarea(attrs = {
                'class': 'form-control',
                'placeholder': 'note'
            })
        }