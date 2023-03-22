from django import forms

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

        self.add_air_conditioning()
        self.add_interrupter()

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
