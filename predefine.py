from Talents_Alliances import Talents, Alliances, Stats

# Stats type
DAMAGE      = 'DAMAGE'
MA_DAMAGE   = 'MA_DAMAGE'
HEALTH      = 'HEALTH'
CRIT        = 'CRIT'
DODGE       = 'DODGE'
ARMOR       = 'ARMOR'
MA_ARMOR    = 'MA_ARMOR'
SPELL_POW   = 'SPELL_POW'

# Fighter classes
TANK        = 'TANK'
MAGE        = 'MAGE'
ARCHER      = 'ARCHER'

# Tank talents

KNIGHT = Talents(
    'KNIGHT',
    TANK,
    [
        Stats(ARMOR, 200, 2250)
    ],
    '''
    All damage taken is reduced by 6-15%
    '''
)

ASSASSIN = Talents(
    'ASSASSIN',
    TANK,
    [
        Stats(DODGE, 60, 570)
    ],
    '''
    Once in a while, the fighter cannot be targeted for 2 - 4 secs
    '''
)

BERSERKER = Talents(
    'BERSERKER',
    TANK,
    [
        Stats(HEALTH, 1580, 41330)
    ],
    '''
    During the battle, the fighter restores 900 - 15000 of\n
    their health every 5 secs
    '''
)

ROGUE = Talents(
    'ROGUE',
    TANK,
    [
        Stats(DAMAGE, 100, 1230)
    ],
    '''
    After dealing 1700 - 30000 damage, the fighter increases\n
    their physical armor by 10 - 30% for 5 secs
    '''
)

BARBARIAN = Talents(
    'BARBARIAN',
    TANK,
    [
        Stats(HEALTH, 1820, 41330),
        Stats(DAMAGE, 110, 1230)
    ],
    '''
    Once in a while, the fighter makes an extra attack that\n
    deal 2400 - 42000 damage to the target and increases the\n
    fighter\'s physical & magic armor by 10 - 30% for 1 sec
    '''
)

NINJA = Talents(
    'NINJA',
    TANK,
    [
        Stats(DODGE, 70, 570),
        Stats(DAMAGE, 110, 1230)
    ],
    '''
    After each 4 attack, the fighter deals critical damage
    '''
)

SAMURAI = Talents(
    'SAMURAI',
    TANK,
    [
        Stats(DODGE, 80, 570),
        Stats(ARMOR, 270, 2250)
    ],
    '''
    Once in a while, the fighter gets a shield that protects\n
    from being stunned or slowed down for 3 secs
    '''
)

CRUSADER = Talents(
    'CRUSADER',
    TANK,
    [
        Stats(HEALTH, 2100, 41330),
        Stats(ARMOR, 270, 2250)
    ],
    '''
    Once in a while, strikes a blow that deals 1700 - 30000\n
    damage within a small area and silences all enemies hit\n
    for 1 - 1.7 secs
    '''
)

# Mage talents
PRIEST = Talents(
    'PRIEST',
    MAGE,
    [
        Stats(HEALTH, 850, 10300)
    ],
    '''
    Once in a while, restores 200 - 4000 health of the fighter\n
    with the least health
    '''
)

SPELL_CASTER = Talents(
    'SPELL_CASTER',
    MAGE,
    [
        Stats(SPELL_POW, 250, 3260)
    ],
    '''
    Once in a while, shoots magic arrows at 3 random enemies,\n
    dealing 200 - 4000 damage (Preferred Target MAGES)
    '''
)

MONK = Talents(
    'MONK',
    MAGE,
    [
        Stats(DODGE, 60, 610)
    ],
    '''
    Once in a while, the fighter\'s spell power is increased by\n
    10 - 20% and by 10 - 20% of their dodge
    '''
)

SHAMAN = Talents(
    'SHAMAN',
    MAGE,
    [
        Stats(MA_DAMAGE, 40, 460)
    ],
    '''
    After dealing 1700 - 30000 damage, the fighter increases\n
    their spell power by 10 - 30% for 3 secs (Effect triggers\n
    once per 7 secs) 
    '''
)

SCHOLAR = Talents(
    'SCHOLAR',
    MAGE,
    [
        Stats(SPELL_POW, 270, 3260),
        Stats(DODGE, 60, 610)
    ],
    '''
    Once in a while, the cooldown of the fighter's weapon abilities are reduced by 1'5 - 1 sec
    '''
)

# NECROMANCER = Talents(
#     '',
#     MAGE,
#     Stats(),
#     ''
# )

# WARLOCK = Talents(
#     '',
#     MAGE,
#     Stats(),
#     ''
# )

# SORCERER = Talents(
#     '',
#     MAGE,
#     Stats(),
#     ''
# )

# # Arch talents

# SNIPER = Talents(
#     '',
#     ARCHER,
#     Stats(),
#     ''
# )

# SENTRY = Talents(
#     '',
#     ARCHER,
#     Stats(),
#     ''
# )

# SLAYER = Talents(
#     '',
#     ARCHER,
#     Stats(),
#     ''
# )

# TRICKSTER = Talents(
#     '',
#     ARCHER,
#     Stats(),
#     ''
# )

# TRACKER = Talents(
#     '',
#     ARCHER,
#     Stats(),
#     ''
# )

# NOMAD = Talents(
#     '',
#     ARCHER,
#     Stats(),
#     ''
# )

# MIRAGE = Talents(
#     '',
#     ARCHER,
#     Stats(),
#     ''
# )

# RANGER = Talents(
#     '',
#     ARCHER,
#     Stats(),
#     ''
# )

# Alliances with 2 Units
SINNERS_CONFESION = Alliances(
    'SINNERS_CONFESION',
    [MONK, ROGUE],
    '''
    Once in a while, the alliance members get a shield that\n
    absorbs 1200 - 3800 magic damage
    '''
)

# DIRTY_DEEDS = Alliances(
#     'DIRTY_DEEDS',
#     [SLAYER, SHAMAN],
#     '''
    
#     '''
# )

# Alliances with 3 Units


# Alliances with 4 Units


# Alliances with 5 Units


ALLIANCES_COLLECTION = [
    
]