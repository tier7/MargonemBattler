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
                character.equipment[key] = get_item_from_db.getItem(element, key)
                print(character.equipment)
    @staticmethod
    def update_common_attributes(character):
        ignoreAttribs = ["id","name","rarity","reqp","lvl","artisanbon", "legbon"]
        for item,stats in character.equipment.items():
            if stats != None:
                for stat,value in stats.items():
                    if value != None and stat == "enfatig":
                        value = value.split(",")
                        character.enfatigChance += int(value[0])
                        if character.enfatigChance > 100:
                            character.enfatigChance = 100
                        character.enfatigVal = max(int(value[1]),character.enfatigVal)
                    elif value != None and stat == "manafatig":
                        value = value.split(",")
                        character.manafatigChance += int(value[0])
                        if character.manafatigChance > 100:
                            character.manafatigChance = 100
                        character.manafatigVal = max(int(value[1]), character.manafatigVal)
                    elif value != None and stat == "da":
                        character.di+= int(value)
                        character.ds+= int(value)
                        character.dz+= int(value)
                    elif value != None and stat == "sa":
                        character.sa = character.sa+int(value)/100
                    elif value != None and stat == "slow":
                        character.slow = character.slow+int(value)/100
                    elif value != None and stat in ["light", "fire", "frost"]:
                        value = value.split(",")
                        if item == "firstHand":
                            character.magicDmgType["firstHand"] = stat
                            if stat == "light":
                                character.magicDmg["firstHand"] = {"min": value[0], "max": value[1]}
                            elif stat == "fire":
                                character.magicDmg["firstHand"] = value[0]
                            else:
                                character.magicDmg["firstHand"] = value[1]
                                if int(value[0]) / 10 > character.weaponSlow["frost"]:
                                    character.weaponSlow["frost"] = int(value[0])/10
                        else:
                            character.magicDmgType["secondHand"] = stat
                            if stat == "light":
                                character.magicDmg["secondHand"] = {"min": value[0], "max": value[1]}
                            elif stat == "fire":
                                character.magicDmg["secondHand"] = value[0]
                            else:
                                character.magicDmg["secondHand"] = value[1]
                                if int(value[0]) > character.weaponSlow["frost"]:
                                    character.weaponSlow["frost"] = int(value[0])/10
                    elif value != None and stat == "dmg":
                        value = value.split(",")
                        if item == "firstHand":
                            character.physicalDmg["firstHand"] = {"min": value[0], "max": value[1]}
                        else:
                            character.physicalDmg["secondHand"] = {"min": value[0], "max": value[1]}
                    elif value != None and stat not in ignoreAttribs:
                        setattr(character, stat, getattr(character, stat) + int(value))


        character.crit = character.crit + 0.02*character.level
        character.hp = character.hp+character.ds*5
        character.critval = character.critval + ((character.ds)/(0.5*character.level))
        character.critmval = character.critmval + ((character.di)/(0.5*character.level))
        character.absorblimit = character.di*7
        character.sa = character.sa + (min(2, 0.02*character.dz)+max(0, 0.002*(character.dz-100)))
        character.evade = character.evade + (character.dz/30)
