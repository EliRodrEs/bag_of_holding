from django.contrib import admin
from .models import (
    BaseItem,
    ItemPrice,
    Weapon,
    Armor,
    Potion,
    Scroll,
    WondrousItem,
    Wand,
    Staff,
    Rod
)

models = [
    BaseItem,
    ItemPrice,
    Weapon,
    Armor,
    Potion,
    Scroll,
    WondrousItem,
    Wand,
    Staff,
    Rod
]

for model in models:
    admin.site.register(model)
