from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=20)
    block_name = models.CharField(max_length=20)
    port = models.CharField(max_length=20)

    def __str__(self):
        return self.name
