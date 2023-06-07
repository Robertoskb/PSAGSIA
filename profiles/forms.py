from django.contrib.auth.forms import UserCreationForm
from profiles.models import PROFILE_USER, User
from django import forms


class SignUpForm(UserCreationForm):
    profile = forms.ChoiceField(choices=PROFILE_USER)
    registration = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['username', 'registration', 'email', 'profile']
