class ClassRoom:
    def __init__(self, name, interrupter=None, air_conditioning=None):
        self.name = name
        self.interrupter = interrupter
        self.air_conditioning = air_conditioning

    @property
    def interrupter_status(self):
        if self.interrupter is not None:
            return self.interrupter.read()

    @property
    def air_conditioning_status(self):
        if self.air_conditioning is not None:
            return self.air_conditioning.read()
