from typing import List, Tuple

class Stats:
    def __init__(self, type: str, min_value: int, max_value: int) -> None:
        self.type = type
        self.min = min_value
        self.max = max_value
        pass

class Talents:
    def __init__(self, name: str, fighter_class: str, stats: List[Stats], extra_mods: str) -> None:
        self.name = name
        self.fighter_class = fighter_class
        self.stats = {}
        for stat in stats:
            self.stats[stat.type] = stat
        self.extra_mods = extra_mods
        pass

class Alliances:
    def __init__(self, name: str, attributes: List[Talents], mods: str) -> None:
        self.name = name
        self.attributes = {}
        for talent in attributes:
            self.attributes[talent.name] = talent
        self.mods = mods

    def get_unit_class(self) -> Tuple:
        tank, mage, arch = 0, 0, 0
        for talent in self.attributes.values():
            if talent.fighter_class == "TANK":
                tank += 1
            elif talent.fighter_class == "MAGE":
                mage += 1
            else:
                arch += 1
        return tank, mage, arch