# from collections import defaultdict

from django import forms

# from django.core.exceptions import ValidationError


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


css_classes = {'interrupter': 'interrupter',
               'air_contioning': 'air-conditioning'}

labels = {'interrupter': 'Luzes', 'air_conditioning': 'Ares-Condicionados'}


class ClassRoomFormBase(forms.Form):
    interrupter = checkbox('Luzes', True, 'interrupter')
    air_conditioning = checkbox('Ares-Condicionados', True, 'air-conditioning')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in ('interrupter', 'air_conditioning'):
            if self.initial.get(field, 0) is None:
                self.fields[field] = checkbox_disabled(labels[field], css_classes[field])  # noqa:E501

            if self.initial.get(field) is False:
                self.fields[field].widget.attrs.pop('checked', None)
