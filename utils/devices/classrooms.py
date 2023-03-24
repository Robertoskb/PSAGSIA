from random import choice, randint

from .not_connected import NOTCONNECTED


class ClassRoom:
    def __init__(self, id, name, interrupter=None, air_conditioning=None):
        self.id = id
        self.name = name
        self.interrupter = interrupter if randint(1, 100) > 4 else NOTCONNECTED
        self.air_conditioning = air_conditioning if randint(
            1, 100) > 4 else NOTCONNECTED

        self.last_interrupter_status = self.interrupter_status
        self.last_air_conditioning_status = self.air_conditioning_status

    @property
    def interrupter_status(self):
        if self.interrupter is NOTCONNECTED:
            self.last_interrupter_status = None

        else:
            self.last_interrupter_status = choice(
                [True, False, True, False, None]
            )

        return self.last_interrupter_status

    @property
    def air_conditioning_status(self):
        if self.air_conditioning is NOTCONNECTED:
            self.last_air_conditioning_status = None

        else:
            self.last_air_conditioning_status = choice(
                [True, False, True, False, None]
            )

        return self.last_air_conditioning_status
