from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from classrooms.forms import (ClassRoomForm, RegisterBlockForm,  # noqa:E501
                              RegisterClassRoomForm)
from classrooms.models import Block, ClassRoom


class BlockView(TemplateView):
    template_name = 'classrooms/pages/block.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        block_id = kwargs.pop('block')

        get_object_or_404(Block, id=block_id)

        classrooms = ClassRoom.objects.filter(block=block_id).order_by('name')

        context['forms_names'] = ((ClassRoomForm(), classroom.name)
                                  for classroom in classrooms)

        context['blocks'] = Block.objects.all().order_by('name')

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


class AllClassroomsView(TemplateView):
    template_name = 'classrooms/pages/block.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        classrooms = ClassRoom.objects.all().order_by('name')

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

        if classroom.block is not None:
            self.success_url = reverse(
                'classrooms:block', args=(classroom.block.id,))
        else:
            self.success_url = reverse('classrooms:all')

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
