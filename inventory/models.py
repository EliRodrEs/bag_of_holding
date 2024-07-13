from django.contrib.auth.models import User
from django.db import models

from .constants import RARITY


class BaseItem(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField("Date created")
    acquisition_date = models.CharField("Date acquired", max_length=200)
    notes = models.TextField()
    rarity = models.CharField(choices=RARITY, max_length=200)
    price = models.JSONField()
    party_owned = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
