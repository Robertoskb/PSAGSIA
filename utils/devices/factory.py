from .classrooms import ClassRoom


def get_device(device):
    ...


def get_classroom(name='Sala 1'):
    return ClassRoom(name, 'interrupter', 'air_conditioning')


def get_classrooms(qty=8):
    return [get_classroom(f'Sala {i+1}') for i in range(qty)]
