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
    Once in a while, the cooldown of the fighter\'s weapon\n
    abilities are reduced by 1'5 - 1 sec
    '''
)

NECROMANCER = Talents(
    'NECROMANCER',
    MAGE,
    [
    Stats(HEALTH, 1000, 10300),
    Stats(MA_DAMAGE, 50, 460)
    ],
    '''
    Each time any fighter is killed on the battlefield,\n
    restores 900 - 15000 of the fighter with the least health
    '''
)

WARLOCK = Talents(
    'WARLOCK',
    MAGE,
    [
    Stats(DODGE, 70, 610),
    Stats(MA_DAMAGE, 50, 460)
    ],
    '''
    When this fighter takes lethal damage, they restore \n
    1100 - 20000 health and gets a shield that absorbs \n
    20 - 25% damage for 5 secs
    '''
)

SORCERER = Talents(
    'SORCERER',
    MAGE,
    [
    Stats(SPELL_POW, 370, 3260),
    Stats(HEALTH, 1150, 10300)
    ],
    '''
    When the battle starts, gets a shield that absorbs 3400 -\n
    60000 damage. While the shield is active, the fighter\'s\n
    spell power is increased by 35 - 50%
    '''
)

# Arch talents

SNIPER = Talents(
    'SNIPER',
    ARCHER,
    [
    Stats(DAMAGE, 100, 2230),
    ],
    '''
    Once in a while, takes a shot that stuns the enemy for \n
    1 sec and deals 110 - 120% more damage
    '''
)

SENTRY = Talents(
    'SENTRY',
    ARCHER,
    [
    Stats(HEALTH, 910, 12090),
    ],
    '''
    The fighter\'s critical hits reduce the taarget\'s \n
    physical armor by 20 - 25% for 4 secs (Stacks up to\n
    3 times)
    '''
)

SLAYER = Talents(
    'SLAYER',
    ARCHER[
    Stats(CRIT, 50, 740)
    ],
    '''
    Once in a while, takes a shot at the target with the \n
    least health. That shot deals 120 - 130% extra damage. \n
    Also, if the shot kills the target, the fighter shoots \n
    at another enemy with the least health
    '''
)

TRICKSTER = Talents(
    'TRICKSTER',
    ARCHER[
    Stats(DODGE, 60, 610),
    ],
    '''
    The fighter\'s crit is increased by 20 - 30% of their dodge
    '''
)

TRACKER = Talents(
    'TRACKER',
    ARCHER,
    [
    Stats(HEALTH, 1180, 12090),
    Stats(DODGE, 60 - 610)
    ],
    '''
    When the fighter dodges an enemy attack, they are given \n
    a charge that enhances their damage by 15 - 20% for 3 secs \n
    (Up to 3 charges at a time)
    '''
)

NOMAD = Talents(
    'NOMAD',
    ARCHER,
    [
    Stats(DODGE, 60, 610),
    Stats(DAMAGE, 140, 2230)
    ],
    '''
    After each 3 shot, the fighter deal () more damage and \n
    ignores 15 - 20% of the target\'s armor
    '''
)

MIRAGE = Talents(
    'MIRAGE',
    ARCHER,
    [
    Stats(CRIT, 70, 740),
    Stats(DODGE, 70, 610)
    ],
    '''
    Once in a while, the fighter completely ignores all physical \n
    damage taken for 4 secs
    '''
)

RANGER = Talents(
    'RANGER',
    ARCHER,
    [
    Stats(CRIT, 70, 740),
    Stats(DAMAGE, 210, 2230)
    ],
    '''
    Once in a while, the fighter takes 3 quick shots at the \n
    same target. Each of the shots deals 200% more damage
    '''
)

# Alliances with 2 Units
SINNERS_CONFESION = Alliances(
    'SINNERS_CONFESION',
    [MONK, ROGUE],
    '''
    Once in a while, the alliance members get a shield that\n
    absorbs 1200 - 3800 magic damage
    '''
)

DIRTY_DEEDS = Alliances(
    'DIRTY_DEEDS',
    [SLAYER, SHAMAN],
    '''
    Each time an alliance archer deals critical damage, all \n
    alliance members have their magic enhanced by 500 - 1500 \n
    for 5 secs 
    '''
)

OPPOSITES_MEET = Alliances(
    'OPPOSITES_MEET',
    [BERSERKER, TRICKSTER],
    '''
    Once in a while, an alliance warrior marks their target. \n
    An alliance archer launches an extra projectile at the \n
    marked target along with each shot. Until target is killed, \n
    all damage done by the archer is enhanced by 200 - 250% \n
    (Mark lasts 4 secs)
    '''
)

PRIESTS_RITUALS = Alliances(
    'PRIESTS_RITUALS',
    [PRIEST, PRIEST],
    '''
    The alliance members restore 30 - 55% more health to \n
    their allies and receive 30 - 55% more healing
    '''
)

SAGITTARIANS = Alliances(
    'SAGITTARIANS',
    [SNIPER, SNIPER],
    '''
    All alliance members have a 30% chance of shooting a \n
    random enemy, dealing 23700 - 75000 damage to them
    '''
)

BROTHERS_KNIGHTS = Alliances(
    'BROTHERS_KNIGHTS',
    [KNIGHT, KNIGHT],
    '''
    When the battle starts, the alliance members get a shield \n
    that absorbs 50600 - 160000 physical damage
    '''
)

IMMORTALS = Alliances(
    'IMMORTALS',
    [ARCHER, MAGE],
    '''
    All alliance members have their dodge increased by 12 - 20% \n
    and their health increased by 12 - 20%
    '''
)

INVINCIBLE = Alliances(
    'INVINCIBLE',
    [TANK, MAGE],
    '''
    All alliance members have their Physical & Magic armor \n
    increased by 5 - 10%
    '''
)

BATTLE_BROTHERS = Alliances(
    'BATTLE_BROTHERS',
    [TANK, ARCHER],
    '''
    All alliance members have their physical damage enhanced \n
    by 40 - 65%
    '''
)

# Alliances with 3 Units
NOT_A_SIMPLE_SAMURAI = Alliances(
    'NOT_A_SIMPLE_SAMURAI',
    [SAMURAI, SORCERER, WARLOCK],
    '''
    Once in a while, an alliance warrior gets a shield that \n
    absorbs 30 - 40% of the damage taken for 3 sec. All alliance \n
    members restore an amount of health equal to 50 - 60% of the \n
    damage taken by the shielded warrior. The healing is distributed equally
    '''
)

CRUSADE = Alliances(
    'CRUSADE',
    [MIRAGE, CRUSADER, BARBARIAN],
    '''
    Once in a while, an alliance archer has a 50% chance of \n
    casting a shield on a warrior that absorbs 50 - 70% of the \n
    physical damage taken for 5 sec. While the shield is active, \n
    the warrior restores an amount of health equal to 40 - 60% of \n
    the damage done by the archer\'s shots
    '''
)

CURSED_RANGERS = Alliances(
    'CURSED_RANGERS',
    [WARLOCK, RANGER, MIRAGE],
    '''
    When the battle starts, the alliance archers have their \n
    damage enhanced by 200% and their crit increased by 2800 -\n
    5000. Also, they have their physical & magic armour reduced \n
    by 20 - 30%. All effect are active as long as the alliance \n
    mage is alive. 
    '''
)

RUN_YOU_FOOLS = Alliances(
    'RUN_YOU_FOOLS',
    [SCHOLAR, BARBARIAN, NINJA],
    '''
    Once in a while, the mage restores an amount of health \n
    equal to the damage the alliance warriors have taken over \n
    3 sec. Then, the mage heals the entire squad and restores \n
    the same amount of health that is distributed equally among \n
    all allies.
    '''
)

BOOKWORMS = Alliances(
    'BOOKWORMS',
    [TRACKER, SCHOLAR, NECROMANCER],
    '''
    After the alliance mage deals 9500 - 22500 damage, all \n
    archers deal critical damage for 5 sec. The effect triggers \n
    once per 9 sec
    '''
)

SEARCH_PARTY = Alliances(
    'SEARCH_PARTY',
    [BARBARIAN, TRACKER, NOMAD],
    '''
    After the alliance archer deals 9500 - 22500 damage, a \n
    warrior gains a charge that increases their physical & \n
    magical armor by 20 - 50% for 3 sec. (Up to 3 charges \n
    at a time)
    '''
)

BRETHREN = Alliances(
    'BRETHREN',
    [SPELL_CASTER, MONK, SHAMAN],
    '''
    Once in a while, each alliance member gets a shield that \n
    absorbs 22 - 32% of the physical damage for 4 sec. The mages\n
    restores an amount of health equal to 35 - 70% of the damage \n
    absorbed by the shields
    '''
)

DEADLY_AND_ELUSIVE = Alliances(
    'DEADLY_AND_ELUSIVE',
    [SENTRY, SLAYER, TRICKSTER],
    '''
    Once in a while, all alliance archers take a shot at a \n
    random target. That shot deals 210 - 300% more damage \n
    and stuns the target for 1'6 sec
    '''
)

MAD_MAN = Alliances(
    'MAD_MAN',
    [TANK, ARCHER],
    '''
    Once in a while, alliance members attack a small area. \n
    Their damage is enhanced by 140 - 270% and is done as \n
    pure damage.
    '''
)

SECRET_SOCIETY = Alliances(
    'SECRET_SOCIETY',
    [PRIEST, SPELL_CASTER, ASSASSIN],
    '''
    Each time an alliance warrior dodges an enemy attack, \n
    the other alliance member\'s spell power is increased \n
    80 - 220% for 3 sec. (This effect doesn\'t stack)
    '''
)

SPELL_CASTERS_TRICKS = Alliances(
    'SPELL_CASTERS_TRICKS',
    [SNIPER, SENTRY, SPELL_CASTER],
    '''
    A mage restores 60 - 150% health to a random alliance \n
    archer of the damage done by normal attacks
    '''
)

EXPEDITION_PARTY = Alliances(
    'EXPEDITION_PARTY',
    [KNIGHT, ASSASSIN, SENTRY],
    '''
    Each time an archer lands a critical hit on an enemy, \n
    a random alliance warrior restores 6200 - 19500 health
    '''
)

BOMBERS = Alliances(
    'BOMBERS',
    [TANK, ARCHER, MAGE],
    '''
    Once in a while, a warrior stuns the target for 0'7 - 1'4 \n
    sec, and archer reduces the target\'s attack speed by 30 \n
    - 50% & mage silences the target for 1'8 - 2'5 sec
    '''
)


# Alliances with 4 Units
UNDER_COVER_OF_NIGHT = Alliances(
    'UNDER_COVER_OF_NIGHT',
    [PRIEST, NECROMANCER, ASSASSIN, NINJA],
    '''
    Once in a while, all alliance members get a shield that \n
    absorbs 30 - 40% of the damage taken for 4 sec. 25 - 44% \n
    of the damaged absorbed is dealt back to the enemy as physical damage
    '''
)

RISEN_FROM_THE_TOMB = Alliances(
    'RISEN_FROM_THE_TOMB',
    [SNIPER, NOMAD, SPELL_CASTER, NECROMANCER],
    '''
    When one of the alliance members is killed, they are resurrected \n
    with their health at 15 - 30% of their max. Also, another \n
    alliance takes damage equal to 40 - 20% of their health \n
    (Triggers 2 - 4 times per battle)
    '''
)

CULTURE_CLASH = Alliances(
    'CULTURE_CLASH',
    [KNIGHT, NINJA, SENTRY, NOMAD],
    '''
    Once in a while, the alliance archers reduce their target\'s \n
    armor by 35 - 60% for 5 sec. Also, they increase the armor of \n
    the allied warriors by 60 - 125% of that value.
    '''
)


# Alliances with 5 Units
ILLUSIONISTS = Alliances(
    'ILLUSIONISTS',
    [MONK, SHAMAN, SCHOLAR, SAMURAI, CRUSADER],
    '''
    Once in a while, 3 random enemies are struck with fear \n
    for 1'2 sec. when the fear wears off, they become unable \n
    to use their weapons for 1'3 sec. Also, the damage done by \n
    the alliance warriors is enhanced by 45 - 70% of the weapon \n
    damage normally done by the fighters that are currently \n
    disarmed by this ability. Last for 3 sec.  
    '''
)

VERY_STRANGE_THINGS = Alliances(
    'VERY_STRANGE_THINGS',
    [SLAYER, TRICKSTER, TRACKER, WARLOCK, SORCERER],
    '''
    Once in a while, an alliance mage increases the crit of \n
    an archer by 120 - 200%. (Stacks up to 4 times). When a \n
    mage dies, the effects applied by them are removed.
    '''
)

FOREST_BANDITS = Alliances(
    'FOREST_BANDITS',
    [BERSERKER, ROGUE, BARBARIAN, MIRAGE, RANGER],
    '''
    Once in a while, the alliance warrior steal 25 - 50% of \n
    the armor from their targets. Alliance archers steal 25 - \n
    50% of the crit from their targets. Also, once in a while, \n
    each alliance member deals 28500 - 90000 physical damage to \n
    their targets over 2'5 sec.
    '''
)

ALLIANCES_COLLECTION = [
SINNERS_CONFESION, 
DIRTY_DEEDS, 
OPPOSITES_MEET, 
PRIESTS_RITUALS, 
SAGITTARIANS, 
BROTHERS_KNIGHTS, 
IMMORTALS, 
INVINCIBLE, 
BATTLE_BROTHERS, 
NOT_A_SIMPLE_SAMURAI, 
CRUSADE, 
CURSED_RANGERS, 
RUN_YOU_FOOLS, 
BOOKWORMS, 
SEARCH_PARTY, 
BRETHREN, 
DEADLY_AND_ELUSIVE, 
MAD_MAN, 
SECRET_SOCIETY, 
SPELL_CASTERS_TRICKS, 
EXPEDITION_PARTY,
BOMBERS, 
UNDER_COVER_OF_NIGHT, 
RISEN_FROM_THE_TOMB, 
CULTURE_CLASH, 
ILLUSIONISTS, 
VERY_STRANGE_THINGS, 
FOREST_BANDITS  
]