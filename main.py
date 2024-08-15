from battle import Battle
import effects
import get_item_from_db
from CharacterCreator import Creator
# Stwórz instancję Warrior
warrior = Creator.create("mage", 300)
Creator.gearUp(warrior, 45483,45488,43698,45486,19930,33294,26575,30119)
warrior2 = Creator.create("mage",300)
Creator.gearUp(warrior2,26314,40551,20099,8533,49868,24661,26575,30119)

Creator.update_common_attributes(warrior)
Creator.update_common_attributes(warrior2)
battle = Battle(warrior,warrior2)
print(battle.battle())