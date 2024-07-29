import get_item_from_db
from CharacterCreator import Creator
# Stwórz instancję Warrior
warrior = Creator.create("mage", 300)

print(f"Level: {warrior.level}, Strength: {warrior.ds}, Dexterity: {warrior.dz}, Intelligence: {warrior.di}, Hp: {warrior.hp}, crit: {warrior.crit}")
Creator.gearUp(warrior, 39730,0,0,0,0,0,0,0)
print(warrior.equipment)
Creator.update_common_attributes(warrior)