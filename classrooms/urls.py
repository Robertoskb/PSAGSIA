from django.urls import path

from classrooms import views

app_name = 'classrooms'

urlpatterns = [
    path('<int:block>/', views.BlockView.as_view(), name='block'),
    path('overview/', views.ClassroomsOverView.as_view(), name='overview'),
    path('classroom/create/', views.ClassRoomRegisterView.as_view(), name='create'),  # noqa:E501
    path('block/create/', views.BlockRegisterView.as_view(), name='block_create'),  # noqa:E501
]
