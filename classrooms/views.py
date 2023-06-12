from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse
from classrooms.forms import ClassRoomForm, RegisterClassRoomForm, RegisterBlockForm  # noqa:E501
from classrooms.models import ClassRoom, Block


class BlockView(TemplateView):
    template_name = 'classrooms/pages/block.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        block_id = kwargs.pop('block')
        classrooms = ClassRoom.objects.filter(block=block_id)

        context['forms_names'] = ((ClassRoomForm(), classroom.name)
                                  for classroom in classrooms)

        context['blocks'] = Block.objects.all().order_by('name')

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


class ClassRoomRegisterView(FormView):
    template_name = 'classrooms/pages/register.html'
    form_class = RegisterClassRoomForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Cadastro de Sala'

        return context

    def form_valid(self, form) -> HttpResponse:
        classroom = form.save()

        self.success_url = reverse(
            'classrooms:block', args=(classroom.block.id,))

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
