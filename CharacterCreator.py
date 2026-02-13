import get_item_from_db
import skills
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
            paladin = Paladin(level)
            return paladin
        elif profession == "hunter":
            return Hunter(level)
        elif profession == "mage":
            mage = Mage(level)
            skills.assign_skills(mage,
            {
            "kula_ognia":0, "lodowy_pocisk":0, "porazenie":0, "zwiekszenie_absorpcji":0,
            "koncentracja_many":0, "sprawnosc_fizyczna":0, "duszacy_pocisk":0, "leczenie_ran":0,
            "fuzja_zywiolow":0, "chwila_skupienia":0, "zdrowa_atmosfera":0, "cios_krytyczny":0,
            "spowalniajace_uderzenie":0, "szadz":0, "rozladowujacy_pocisk":0, "rytualne_szaty":0,
            "magiczna_oslona":0, "wrodzona_szybkosc":0, "potega_ognia":0, "potega_zimna":0,
            "potega_blyskawic":0, "moc_leczenia":0, "krytyczna_potega":0, "przetrwanie":0,
            "stopiona_skora":0, "mrozne_sople":0, "wyladowanie_energii":0, "determinacja":0,
            "apogeum":0, "wzmocniony_pancerz":0, "plonaca_bariera":0, "lodowa_bariera":0,
            "elektryczna_bariera":0, "wytrwalosc_elementalisty":0, "oslabienie":0,
            "trwalosc_mocy":0, "wewnetrzny_spokoj":0, "klatwa":0, "zrodlo_potegi":0,
            "platnerstwo":0, "konskie_zdrowie":0, "strach":0})
            return mage
        elif profession == "tracker":
            return Tracker(level)
        elif profession == "blade-dancer":
            return BladeDancer(level)
        elif profession == "warrior":
            return Warrior(level)
        else:
            raise ValueError(f"Unknown character type: {profession}")

    @staticmethod
    # equipment
    def gearUp(character, helmetID, necklaceID, ringID, glovesID, armorID, bootsID, firstHandID, secondHandID):
        eqElements = {'helmet':helmetID, 'necklace':necklaceID, 'ring':ringID, 'gloves':glovesID, 'armor':armorID, 'boots':bootsID, 'firstHand':firstHandID, 'secondHand':secondHandID}
        for key,element in eqElements.items():
            if element != 0:
                character.equipment[key] = get_item_from_db.getItem(element, key)

    @staticmethod
    def update_common_attributes(character):
        ignoreAttribs = ["id", "name", "rarity", "reqp", "lvl", "artisanbon", "legbon"]
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
                    elif value != None and stat == "light":
                        value = value.split(",")
                        character.damage[stat] += int(value[0])
                    elif value != None and stat == "frost":
                        value = value.split(",")
                        character.weaponSlow[stat] += int(value[0])/100
                        character.damage[stat] += int(value[1])
                    elif value != None and stat == "fire":
                        character.damage[stat] += int(value)
                    elif value != None and stat == "dmg":
                        value = value.split(",")
                        character.damage[stat] += (int(value[0])+int(value[1]))/2

                    elif value != None and stat not in ignoreAttribs:
                        setattr(character, stat, getattr(character, stat) + int(value))


        character.crit = character.crit + 0.02*character.level
        character.hp = character.hp+character.ds*5
        character.critval = character.critval + ((character.ds)/(0.5*character.level))
        character.critmval = character.critmval + ((character.di)/(0.5*character.level))
        character.absorblimit = character.di*7
        character.sa = character.sa + (min(2, 0.02*character.dz)+max(0, 0.002*(character.dz-100)))
        character.evade = character.evade + (character.dz/30)


