from django.urls import path

from classrooms import views

app_name = 'classrooms'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
