from django.views.generic.base import TemplateView
from classrooms.forms import ClassRoomForm, ClassRoom, Block
from django.shortcuts import get_object_or_404


class BlockView(TemplateView):
    template_name = 'classrooms/pages/block.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        block_id = kwargs.pop('block')

        block = get_object_or_404(Block, id=block_id)

        classrooms = ClassRoom.objects.filter(block=block_id).order_by('name')

        context.update({
            'forms_names': ((ClassRoomForm(), classroom.name) for classroom in classrooms),  # noqa:E501
            'blocks': Block.objects.all().order_by('name'),
            'title': block.name,
        })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


class ClassroomsOverView(TemplateView):
    template_name = 'classrooms/pages/block.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        classrooms = ClassRoom.objects.all().order_by('name')  # noqa:E501

        context.update({
            'forms_names': ((ClassRoomForm(), classroom.name) for classroom in classrooms),  # noqa:E501
            'blocks': Block.objects.all().order_by('name'),
            'title': 'Overview',
        })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)
