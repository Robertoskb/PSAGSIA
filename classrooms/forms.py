from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError


def checkbox_disabled(label, class_name):
    class_name += f' {class_name}-disabled'

    return forms.BooleanField(
        label=label, required=False,
        widget=forms.CheckboxInput(attrs={
            'disabled': True, 'class': class_name,
        }))


def checkbox(label, initial, class_name):
    if initial is None:
        return checkbox_disabled(label, class_name)

    return forms.BooleanField(
        required=False,
        label=label, initial=initial,
        widget=forms.CheckboxInput(attrs={'class': class_name, }))


def add_field(classroom, name_field, label, class_name):
    if getattr(classroom, name_field) is not None:
        status = getattr(classroom, f'last_{name_field}_status')

        return checkbox(label, status, class_name)


def get_classroom_form(class_room, *args, **kwargs):
    class ClassRoomFormBase(forms.Form):
        classroom = class_room

        interrupter = add_field(classroom, 'interrupter', 'luzes', 'interrupter')  # noqa: E501
        air_conditioning = add_field(classroom, 'air_conditioning', 'Ares-Condicionados', 'air-conditioning')  # noqa: E501

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._my_errors = defaultdict(list)

        def clean(self):
            if self._my_errors:
                raise ValidationError(self._my_errors)

            return super().clean()

        def clean_interrupter(self):
            field_name = 'interrupter'
            field_value = self.cleaned_data.get(field_name)

            if self.classroom.last_interrupter_status is None:
                return

            changed = 'ligar' if field_value else 'desligar'

            self._my_errors[field_name].append(
                f'Falha ao tentar {changed} as luzes')

            return field_value

        def clean_air_conditioning(self):
            field_name = 'air_conditioning'
            field_value = self.cleaned_data.get(field_name)

            if self.classroom.last_air_conditioning_status is None:
                return

            changed = 'ligar' if field_value else 'desligar'

            self._my_errors[field_name].append(
                f'Falha ao tentar {changed} os ares-condicionados')

            return field_value

    return ClassRoomFormBase(*args, **kwargs)
