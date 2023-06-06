from django.urls import path

from classrooms import views

app_name = 'classrooms'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('classroom/create', views.ClassRoomRegisterView.as_view(), name='create'),  # noqa:E501
]
