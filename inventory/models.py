from typing import Optional

from django.db import models
from django.contrib.auth.models import User
from bag_of_holding.inventory.constants import RARITY_CHOICES, WEAPON_TYPE_CHOICES, ARMOR_TYPE_CHOICES, RECHARGE_TYPES
from django.utils.translation import gettext_lazy as _


class BaseItem(models.Model):
    name: str = models.CharField(max_length=200)
    creation_date: models.DateTimeField = models.DateTimeField(_("Date created"))
    acquisition_date: Optional[str] = models.CharField(_("Date acquired"), max_length=200)
    notes: Optional[str] = models.TextField()
    price: dict = models.JSONField()  # type hint for JSONField
    party_owned: bool = models.BooleanField(default=False)
    available: bool = models.BooleanField(default=True)
    owner: User = models.ForeignKey(User, on_delete=models.CASCADE)
    rarity: str = models.CharField(choices=RARITY_CHOICES, max_length=200, default='common')
    description: Optional[str] = models.TextField()
    attunement_required: bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        abstract = True


class RechargeableItem(models.Model):
    name: str = models.CharField(max_length=200)
    charges: [int] = models.IntegerField(default=0, help_text=_("Remaining charges"), blank=True,
                                         null=True)
    max_charges: [int] = models.IntegerField(default=0, help_text=_("Maximum charges"), blank=True,
                                             null=True)
    recharge_type: str = models.CharField(choices=RECHARGE_TYPES, max_length=200)

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
    weapon_type: str = models.CharField(choices=WEAPON_TYPE_CHOICES, max_length=50)
    damage: str = models.CharField(max_length=50)
    properties: str = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Weapon")})'


class Armor(BaseItem):
    armor_type: str = models.CharField(choices=ARMOR_TYPE_CHOICES, max_length=50)
    armor_class: str = models.CharField(max_length=50)
    strength_requirement: Optional[int] = models.IntegerField(null=True, blank=True)
    stealth_disadvantage: bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name} ({_("Armor")})'


class Potion(BaseItem):
    effect: str = models.TextField()
    duration: Optional[str] = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name} ({_("Potion")})'


class Scroll(BaseItem):
    spell_name: str = models.CharField(max_length=200)
    spell_level: int = models.IntegerField()
    spell_effects: str = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Scroll")})'


class WondrousItem(BaseItem, RechargeableItem):
    effect: str = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Wondrous Item")})'


class Wand(BaseItem, RechargeableItem):
    effect: str = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Wand")})'


class Staff(BaseItem, RechargeableItem):
    effect: str = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Staff")})'


class Rod(BaseItem, RechargeableItem):
    effect: str = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} ({_("Rod")})'
