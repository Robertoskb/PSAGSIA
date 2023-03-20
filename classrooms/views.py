from django.views.generic.base import TemplateView

from utils.devices import factory


class HomeView(TemplateView):
    template_name = 'classrooms/pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['classrooms'] = factory.get_classrooms()

        return context
