from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from classrooms.forms import ClassRoomForm, RegisterClassRoomForm

classrooms = range(10)


class HomeView(TemplateView):
    template_name = 'classrooms/pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['forms'] = [ClassRoomForm(initial={'interrupter': None})
                            for _ in classrooms]

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


class ClassRoomRegisterView(FormView):
    template_name = 'classrooms/pages/classroom_register.html'
    form_class = RegisterClassRoomForm
