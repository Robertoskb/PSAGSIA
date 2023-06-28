from django.urls import reverse
from classrooms.forms import RegisterClassRoomForm, RegisterBlockForm
from django.views.generic.edit import FormView
from django.http import HttpResponse


class ClassRoomRegisterView(FormView):
    template_name = 'classrooms/pages/register.html'
    form_class = RegisterClassRoomForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Cadastro de Sala'

        return context

    def form_valid(self, form) -> HttpResponse:
        classroom = form.save()

        if classroom.block is not None:
            self.success_url = reverse(
                'classrooms:block', args=(classroom.block.id,))
        else:
            self.success_url = reverse('classrooms:overview')

        return super().form_valid(form)


class BlockRegisterView(FormView):
    template_name = 'classrooms/pages/register.html'
    form_class = RegisterBlockForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Cadastro de Ambiente'

        return context

    def form_valid(self, form) -> HttpResponse:
        block = form.save()

        self.success_url = reverse('classrooms:block', args=(block.id,))

        return super().form_valid(form)
