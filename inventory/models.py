from django.db import models

from bag_of_holding.inventory.constants import RARITY
from bag_of_holding.user.models import User


# Create your models here.
class BaseItem(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField("Date created")
    acquisition_date = models.CharField("Date acquired")
    notes = models.TextField()
    rarity = models.CharField(choices=RARITY)
    price = models.JSONField()
    party_owned = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
