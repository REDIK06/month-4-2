from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField(default=100)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

