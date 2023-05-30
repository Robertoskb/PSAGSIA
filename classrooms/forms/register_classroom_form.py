from django import forms


class RegisterClassRoomForm(forms.Form):
    name = forms.CharField(required=True, max_length=20)
    block_name = forms.CharField(required=True, max_length=20)
    port = forms.CharField(required=True, max_length=20)
