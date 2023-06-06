from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from classrooms.forms import ClassRoomForm, RegisterClassRoomForm
from classrooms.models import ClassRoom


class HomeView(TemplateView):
    template_name = 'classrooms/pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['forms_names'] = [(ClassRoomForm(initial={'interrupter': None}),
                                   classroom.name)
                                  for classroom in ClassRoom.objects.all()]

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


class ClassRoomRegisterView(FormView):
    template_name = 'classrooms/pages/classroom_register.html'
    form_class = RegisterClassRoomForm
    success_url = reverse_lazy('classrooms:create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Cadastro de Sala'

        return context

    def form_valid(self, form) -> HttpResponse:
        form.save()

        return super().form_valid(form)
