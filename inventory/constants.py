from django.utils.translation import gettext_lazy as _

RARITY_CHOICES = [
    ('common', _('Common')),       # Indicates a non-magical item
    ('uncommon', _('Uncommon')),
    ('rare', _('Rare')),
    ('very_rare', _('Very Rare')),
    ('legendary', _('Legendary'))
]

WEAPON_TYPE_CHOICES = [
    ('melee', _('Melee')),
    ('ranged', _('Ranged')),
]

ARMOR_TYPE_CHOICES = [
    ('light', _('Light')),
    ('medium', _('Medium')),
    ('heavy', _('Heavy')),
    ('shield', _('Shield')),
]

RECHARGE_TYPES = [
    ('dawn', _('dawn')),
    ('long_r', _('long rest')),
    ('short_r', _('short rest')),
    ('dusk', _('dusk')),
    ('other', _('other')),
]