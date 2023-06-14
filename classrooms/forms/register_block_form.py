from django import forms
from classrooms.models import Block
from collections import defaultdict


class RegisterBlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = ('name',)
        labels = {'name': 'Nome do bloco'}
