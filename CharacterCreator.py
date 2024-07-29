import get_item_from_db
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

    @staticmethod
    def gearUp(character, helmetID, necklaceID, ringID, glovesID, armorID, bootsID, firstHandID, secondHandID):

        eqElements = {'helmet':helmetID, 'necklace':necklaceID, 'ring':ringID, 'gloves':glovesID, 'armor':armorID, 'boots':bootsID, 'firstHand':firstHandID, 'secondHand':secondHandID}
        for key,element in eqElements.items():
            if element != 0:
                character.equipment.append(get_item_from_db.getItem(element, key))
                print(get_item_from_db.getItem(element, key))
    @staticmethod
    def update_common_attributes(character):
        for item in character.equipment:
            for stat, value in item.items():
                if value != "None":
                    character.stat += value
        character.crit = character.crit + 0.02*character.level
        character.hp = character.hp+character.ds*5
        character.critval = character.critval + ((character.ds)/(0.5*character.level))
        character.critmval = character.critval + ((character.di)/(0.5*character.level))
        character.absorblimit = character.di*7
        character.sa = character.sa + (min(2, 0.02*character.dz)+max(0, 0.002*(character.dz-100)))
        character.evade = character.evade + (character.dz/30)
