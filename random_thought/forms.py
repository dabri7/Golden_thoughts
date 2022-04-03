from django import forms
from random_thought.models import Thought


class AddThought(forms.ModelForm):
    class Meta:
        model = Thought
        fields = '__all__'
        labels = {
            'thought': 'Złota myśl',
            'authot': 'Autor: ',
        }

