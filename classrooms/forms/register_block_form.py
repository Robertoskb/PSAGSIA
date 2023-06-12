from django import forms
from classrooms.models import Block


class RegisterBlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = ('name',)
