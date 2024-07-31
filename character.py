from get_item_from_db import getItem
class Character:
    def __init__(self, level):
        self.equipment = {"helmet":None, "necklace":None, "ring":None, "gloves":None, "armor":None, "boots":None, "firstHand":None, "secondHand":None}
        self.pdmg = {"min":0, "max":0}
        self.mdmg = {"min":0, "max":0}
        self.level = level
        self.dmg = 0
        self.da = 0  # wszycstkie cechy
        self.ds = 4  # siła
        self.dz = 3  # zręczność
        self.di = 3  # intelekt
        self.sa = 1  # szybkość
        self.hp = 20 * min(level, 300)**1.375  # życie
        self.heal = 0  # leczenie
        self.ac = 0  # pancerz
        self.act = 0  # odporność na trucizny
        self.blok = 0  # blok
        self.evade = 0  # unik
        self.acdmg = 0  # niszczenie pancerza
        self.resdmg = 0  # niszczenie odporności
        self.adest = 0  # obniżanie przywracania życia
        self.absorb = 0  # absorpcja fizyczna
        self.absorbm = 0  # absorpcja magiczna
        self.manabon = 0  # mana
        self.energybon = 50  # energia
        self.slow = 0  # obniżanie SA przeciwnika
        self.crit = 1  # cios krytyczny
        self.critval = 120  # siła krytyka fizycznego
        self.critmval = 120  # siła krytyka magicznego
        self.lowcrit = 0  # obniżanie szansy na krytyk
        self.enfatigVal = 0  # losowe niszczenie energii
        self.manafatigVal = 0  # losowe niszczenie many
        self.enfatigChance = 0
        self.manafatigChance = 0
        self.lowevade = 0  # obniżanie uniku
        self.resfire = 0  # odporność na ogień
        self.resfrost = 0  # odporność na zimno
        self.reslight = 0  # odporność na błyskawice
        self.act = 0 # odpornosc na trucizne
        self.pierce = 0  # przebicie pancerza
        self.pierceb = 0  # blok przebicia pancerza
        self.contra = 0  # szansa na kontrę
        self.absdest = 0  # niszczenie absorpcji
        self.absorblimit = 0 #limit absorbcji

    def __str__(self):
        equipment_str = "\n".join(
             f"{item.upper()}: {stats['name']}, {stats['lvl']}"
            for item, stats in self.equipment.items()
            if stats is not None
        )
        return (f"Level: {self.level} \n"
                f"-----------------------\n"
                f"EQUIPMENT\n"
                f"{equipment_str}\n"
                f"-----------------------\n"
                f"ATTACK\n"
                f"Physical dmg: {str(self.pdmg["min"])}-{str(self.pdmg["max"])}\n"
                f"Magic dmg: {str(self.mdmg["min"])}-{str(self.mdmg["max"])}\n"
                f"SA: {self.sa}\n"
                f"Crit chance: {self.crit}\n"
                f"Physical crit strenght: {self.critval}\n"
                f"Magical crit strenght: {self.critmval}\n"
                f"Slow: {self.slow}\n"
                f"Armor destruction: {self.acdmg}\n"
                f"Resist destruction: {self.resdmg}% \n"
                f"-----------------------\n"
                f"DEFENCE\n"
                f"Health: {self.hp} \n"
                f"Armor: {self.ac}\n"
                f"Evade: {self.evade}\n"
                f"Block: {self.blok}\n"
                f"Heal: {self.hp}\n"
                f"Physical absorption: {self.absorb}\n"
                f"Magical absortpion: {self.absorbm}\n"
                f"Mana destruction: {self.manafatigVal} - {self.manafatigChance}%\n"
                f"Energy destruction: {self.enfatigVal} - {self.enfatigChance}%\n"
                f"RESISTS\n"
                f"Fire resist: {self.resfire}\n"
                f"Lightning resist: {self.reslight}\n"
                f"Frost resist: {self.resfrost}\n"
                f"Poison resist: {self.act}\n"
                f"-----------------------\n"
                f"RESOURCES\n"
                f"Mana: {self.manabon}\n"
                f"Energy: {self.energybon}\n"
                f"-----------------------\n"
                f"BASICS\n"
                f"Strength: {self.ds} \n"
                f"Dexterity: {self.dz} \n"
                f"Intelligence: {self.di} \n")

