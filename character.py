from get_item_from_db import getItem
class Character:
    def __init__(self, level):
        self.equipment = []
        self.level = level
        self.dmg = 0
        self.da = 0  # wszystkie cechy
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
        self.acmdmg = 0  # niszczenie odporności
        self.adest = 0  # obniżanie przywracania życia
        self.absorb = 0  # absorpcja fizyczna
        self.absorbm = 0  # absorpcja magiczna
        self.manabon = 0  # mana
        self.energybon = 50  # energia
        self.slow = 0  # obniżanie SA przeciwnika
        self.crit = 1  # cios krytyczny
        self.critval = 0  # siła krytyka fizycznego
        self.critmval = 0  # siła krytyka magicznego
        self.lowcrit = 0  # obniżanie szansy na krytyk
        self.enfatig = 0  # losowe niszczenie energii
        self.manafatig = 0  # losowe niszczenie many
        self.lowevade = 0  # obniżanie uniku
        self.resfire = 0  # odporność na ogień
        self.resfrost = 0  # odporność na zimno
        self.reslight = 0  # odporność na błyskawice
        self.pierce = 0  # przebicie pancerza
        self.pierceb = 0  # blok przebicia pancerza
        self.contra = 0  # szansa na kontrę
        self.absdest = 0  # niszczenie absorpcji
        self.absorblimit = 0 #limit absorbcji
        self.update_common_attributes()

