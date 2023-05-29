from django.views.generic.base import TemplateView

from classrooms.forms import ClassRoomFormBase

classrooms = range(10)


class HomeView(TemplateView):
    template_name = 'classrooms/pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['forms'] = [ClassRoomFormBase(initial={'interrupter': None})
                            for _ in classrooms]

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)
