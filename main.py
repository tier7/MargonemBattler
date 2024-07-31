import get_item_from_db
from CharacterCreator import Creator
# Stwórz instancję Warrior
warrior = Creator.create("mage", 300)
Creator.gearUp(warrior, 45483,45488,43698,45486,19930,33294,0,0)
Creator.update_common_attributes(warrior)
print(warrior)