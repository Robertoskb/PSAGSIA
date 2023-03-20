import random

import serial


class DeviceBase:
    """
    Classe base para simular a conexão de dispositivos,
    mas provavelmente usaremos uma lib externa
    """

    def __init__(self, ip_address):
        # Faz a conexão

        self.ip_address = ip_address

    def switch_on(self):
        # liga
        ...

    def switch_off(self):
        # desliga
        ...

    def __del__(self):
        # Desconecta
        ...
