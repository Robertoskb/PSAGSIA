from django.urls import path

from profiles import views

app_name = 'profiles'

urlpatterns = [
    path("profile/create", views.SignUpView.as_view(), name="create")]
