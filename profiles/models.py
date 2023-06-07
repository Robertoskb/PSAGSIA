from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

PROFILE_USER = (
    ('1', 'Administrator'),
    ('2', 'Server Manager'),
    ('3', 'Visitor'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='3')
    registration = models.CharField(max_length=25)
    profile = models.CharField(max_length=13, choices=PROFILE_USER)

    def __str__(self):
        return self.profile
