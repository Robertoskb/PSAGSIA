from django.contrib import admin
from classrooms.models import ClassRoom, Block


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    ...


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    ...
