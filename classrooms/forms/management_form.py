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


class ClassRoomForm(forms.Form):
    AC_CHOICES = [
        ('turn_on_ac', 'Ligar Ar-Condicionado'),
        ('turn_off_ac', 'Desligar Ar-Condicionado'),
    ]
    LIGHT_CHOICES = [
        ('turn_on_light', 'Ligar Luzes'),
        ('turn_off_light', 'Desligar Luzes'),
    ]

    ac_control = forms.ChoiceField(
        choices=AC_CHOICES, widget=forms.RadioSelect)
    light_control = forms.ChoiceField(
        choices=LIGHT_CHOICES, widget=forms.RadioSelect)

    def __init__(self, *args, initial_ac='turn_off_ac',
                 initial_light='turn_on_light', **kwargs):

        super().__init__(*args, **kwargs)
        if initial_ac is not None:
            self.fields['ac_control'].initial = initial_ac
        if initial_light is not None:
            self.fields['light_control'].initial = initial_light
