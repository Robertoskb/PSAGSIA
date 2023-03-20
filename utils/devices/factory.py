from serial import SerialException, SerialTimeoutException

from .air_conditioning import AirConditioning
from .classrooms import ClassRoom
from .interrupter import Interrupter


def get_device(device):
    try:
        return device()
    except [SerialException, SerialTimeoutException]:
        return None


def get_classroom(name='Sala 1'):
    air_conditioning = get_device(AirConditioning)
    interrupter = get_device(Interrupter)

    return ClassRoom(name, interrupter, air_conditioning)


def get_classrooms(qty=8):
    return [get_classroom(f'Sala {i+1}') for i in range(qty)]
