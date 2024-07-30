import get_item_from_db
from CharacterCreator import Creator
# Stwórz instancję Warrior
warrior = Creator.create("mage", 300)

print(f"Level: {warrior.level}, Strength: {warrior.ds}, Dexterity: {warrior.dz}, Intelligence: {warrior.di}, Hp: {warrior.hp}, crit: {warrior.crit}")
Creator.gearUp(warrior, 45483,0,0,0,0,0,0,0)
Creator.update_common_attributes(warrior)
print(warrior)