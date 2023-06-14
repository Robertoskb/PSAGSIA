from django import forms
from classrooms.models import ClassRoom


class RegisterClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ('name', 'block', 'port')

        labels = {
            'name': 'Nome da sala',
            'block': 'Bloco',
            'port': 'Porta'
        }
