from django import forms
from classrooms.models import ClassRoom


class RegisterClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ('name', 'block', 'port')
