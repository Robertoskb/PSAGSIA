import random

from serial import Serial, SerialException, SerialTimeoutException


def random_exception(self, *args, **kwargs):
    rand = random.randint(1, 100)

    if 2 < rand < 4:
        raise SerialException

    elif rand < 2:
        raise SerialTimeoutException


class DeviceBase(Serial):
    """
    Classe base para simular a conexão de dispositivos,
    mas provavelmente usaremos uma lib externa
    """
    dictionary = Serial.__dict__
    for method in dictionary:
        if callable(dictionary[method]):
            setattr(Serial, method, lambda *a, **k: random_exception(*a, **k))

    def isOpen(self):
        random_exception(self)
        return random.choice([True, False])

    def read(self, *args, **kwargs):
        random_exception(self)

        return random.choice([True, False])


if __name__ == '__main__':
    ser = DeviceBase('')

    print(ser.isOpen())
