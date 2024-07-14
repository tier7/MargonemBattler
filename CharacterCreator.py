from professions.paladin import Paladin
from professions.warrior import Warrior
from professions.hunter import Hunter
from professions.mage import Mage
from professions.tracker import Tracker
from professions.bladeDancer import BladeDancer
class Creator:
    @staticmethod
    def create(profession, level):
        if profession == "paladin":
            return Paladin(level)
        elif profession == "hunter":
            return Hunter(level)
        elif profession == "mage":
            return Mage(level)
        elif profession == "tracker":
            return Tracker(level)
        elif profession == "blade-dancer":
            return BladeDancer(level)
        elif profession == "warrior":
            return Warrior(level)
        else:
            raise ValueError(f"Unknown character type: {profession}")
