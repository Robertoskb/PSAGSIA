from collections import defaultdict
from random import randint

from django import forms
from django.core.exceptions import ValidationError

from utils.devices import ClassRoom


def checkbox_disabled(label, class_name):
    class_name += f' {class_name}-disabled'

    return forms.BooleanField(
        label=label,
        widget=forms.CheckboxInput(attrs={
            'disabled': True, 'class': class_name,
        }))


def checkbox(label, initial, class_name):
    if initial is None:
        return checkbox_disabled(label, class_name)

    return forms.BooleanField(
        label=label, initial=initial,
        widget=forms.CheckboxInput(attrs={'class': class_name, }))


class ClassRoomForm(forms.Form):

    def __init__(self, classroom: ClassRoom, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.classroom = classroom

        # adiciona e configura os campos dinamicamente

        self.add_air_conditioning()
        self.add_interrupter()

        self._my_errors: dict = defaultdict(list)

    def add_air_conditioning(self):
        classroom = self.classroom
        name_field = 'air_conditioning'
        label = 'Ares-Condicionados'
        class_name = 'air-conditioning'

        if classroom.air_conditioning is not None:
            status = classroom.air_conditioning_status

            self.fields[name_field] = checkbox(label, status, class_name)

    def add_interrupter(self):
        classroom = self.classroom
        name_field = 'interrupter'
        label = 'Luzes'
        class_name = 'interrupter'

        if classroom.interrupter is not None:
            status = classroom.interrupter_status

            self.fields[name_field] = checkbox(label, status, class_name)

    def clean(self):
        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super().clean()

    def clean_interrupter(self):
        field_name = 'interrupter'
        field_value = self.cleaned_data.get(field_name)

        changed = 'ligar' if field_value else 'desligar'

        if randint(0, 1) == 1:
            self._my_errors[field_name].append(f'Falha ao tentar {changed}')

    def clean_air_conditioning(self):
        field_name = 'air_conditioning'
        field_value = self.cleaned_data.get(field_name)

        changed = 'ligar' if field_value else 'desligar'

        if randint(0, 1) == 1:
            self._my_errors[field_name].append(f'Falha ao tentar {changed}')
