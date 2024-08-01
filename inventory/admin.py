from django.contrib import admin
from .models import (
    BaseItem,
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
