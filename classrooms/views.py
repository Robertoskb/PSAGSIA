from django.views.generic.base import TemplateView

from classrooms.forms import ClassRoomForm
from utils.devices import factory


class HomeView(TemplateView):
    template_name = 'classrooms/pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['forms'] = (ClassRoomForm(f) for f in factory.get_classrooms())

        return context
