from random import choice, randint

from .not_connected import NOTCONNECTED


class ClassRoom:
    def __init__(self, name, interrupter=None, air_conditioning=None):
        self.name = name
        self.interrupter = interrupter if randint(1, 100) > 4 else NOTCONNECTED
        self.air_conditioning = air_conditioning if randint(
            1, 100) > 4 else NOTCONNECTED

    @property
    def interrupter_status(self):
        if self.interrupter is NOTCONNECTED:
            return None

        if self.interrupter is not None:
            return choice([True, False, True, False, None])

    @property
    def air_conditioning_status(self):
        if self.interrupter is NOTCONNECTED:
            return None

        if self.air_conditioning is not None:
            return choice([True, False, True, False, None])
