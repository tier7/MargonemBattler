import get_item_from_db
from CharacterCreator import Creator
# Stwórz instancję Warrior
warrior = Creator.create("mage", 300)

print(f"Level: {warrior.level}, Strength: {warrior.ds}, Dexterity: {warrior.dz}, Intelligence: {warrior.di}, Hp: {warrior.hp}, crit: {warrior.crit}")
item = get_item_from_db.getItem(9440,'armor')
print(item)
for key, value in item.items():
        print(f"{key}: {value}")