from typing import Optional

from django.db import models
from django.contrib.auth.models import User
from .constants import RARITY_CHOICES, WEAPON_TYPE_CHOICES, ARMOR_TYPE_CHOICES, RECHARGE_TYPES
from django.utils.translation import gettext_lazy as _


class ItemPrice(models.Model):
    pp = models.FloatField(null=True, blank=True)
    ep = models.FloatField(null=True, blank=True)
    gp = models.FloatField(null=True, blank=True)
    sp = models.FloatField(null=True, blank=True)
    cp = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'gp: {self.gp} - sp: {self.sp} - cp: {self.cp}'


class BaseItem(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(_("Date created"))
    acquisition_date = models.CharField(_("Date acquired"), max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    price = models.OneToOneField(ItemPrice, on_delete=models.CASCADE, related_name='base_item')
    is_party_owned = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rarity = models.CharField(choices=RARITY_CHOICES, max_length=200, default='common')
    description = models.TextField(default="", null=True, blank=True)
    attunement_required = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}'


class RechargeableItem(models.Model):
    name = models.CharField(max_length=200)
    charges = models.IntegerField(default=0, help_text=_("Remaining charges"), blank=True, null=True)
    max_charges = models.IntegerField(default=0, help_text=_("Maximum charges"), blank=True, null=True)
    recharge_type = models.CharField(choices=RECHARGE_TYPES, max_length=200)

    class Meta:
        abstract = True

    def use_charge(self) -> bool:
        if self.charges is not None and self.charges > 0:
            self.charges -= 1
            self.save()
            return True
        return False

    def recharge(self) -> None:
        if self.max_charges is not None:
            self.charges = self.max_charges
            self.save()

    def __str__(self) -> str:
        return f'{self.name} ({_("Rechargeable Item")})'


class Weapon(BaseItem):
    weapon_type = models.CharField(choices=WEAPON_TYPE_CHOICES, max_length=50)
    damage = models.CharField(max_length=50)
    properties = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Weapon")})'


class Armor(BaseItem):
    armor_type = models.CharField(choices=ARMOR_TYPE_CHOICES, max_length=50)
    armor_class = models.CharField(max_length=50)
    strength_requirement = models.IntegerField(null=True, blank=True)
    stealth_disadvantage = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name} ({_("Armor")})'


class Potion(BaseItem):
    effect = models.TextField()
    duration = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name} ({_("Potion")})'


class Scroll(BaseItem):
    spell_name = models.CharField(max_length=200)
    spell_level = models.IntegerField()
    spell_effects = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Scroll")})'


class WondrousItem(BaseItem, RechargeableItem):
    effect = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Wondrous Item")})'


class Wand(BaseItem, RechargeableItem):
    effect = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Wand")})'


class Staff(BaseItem, RechargeableItem):
    effect = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Staff")})'


class Rod(BaseItem, RechargeableItem):
    effect = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Rod")})'
