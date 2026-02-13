import skills
from battle import Battle
import effects
import get_item_from_db
from CharacterCreator import Creator
# Stwórz instancję Warrior
warrior = Creator.create("mage", 300)
Creator.gearUp(warrior, 9395,0,0,0,18216,0,26521,0)
warrior2 = Creator.create("mage",300)
Creator.gearUp(warrior2, 0,0,0,0,18216,0,26521,0)
Creator.update_common_attributes(warrior)
Creator.update_common_attributes(warrior2)
print(warrior)
print(warrior2)
battle = Battle(warrior,warrior2)
print(battle.battle())