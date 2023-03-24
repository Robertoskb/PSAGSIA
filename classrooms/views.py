from django.views.generic.base import TemplateView

from classrooms.forms import get_classroom_form
from utils.devices import factory

classrooms = None


class HomeView(TemplateView):
    template_name = 'classrooms/pages/home.html'

    def get_context_data(self, **kwargs):
        global classrooms

        context = super().get_context_data(**kwargs)

        classrooms = factory.get_classrooms()

        context['forms'] = [get_classroom_form(c) for c in classrooms]

        return context

    def post(self, request, *args, **kwargs):
        global classrooms

        id = int(request.POST.get('id'))
        classroom = classrooms[id]

        form = get_classroom_form(classroom, request.POST)
        form.is_valid()

        classroom.interrupter_status
        classroom.air_conditioning_status

        context = self.get_context_data(**kwargs)
        classrooms[id] = classroom

        forms = context['forms']

        forms[id] = get_classroom_form(classroom)
        forms[id]._errors = form._errors

        return self.render_to_response(context)
