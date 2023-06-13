from django.db import models


class Block(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class ClassRoom(models.Model):
    name = models.CharField(max_length=20)
    block = models.ForeignKey(
        Block, null=True, on_delete=models.SET_NULL, blank=True)
    port = models.CharField(max_length=20)

    def __str__(self):
        return self.name
