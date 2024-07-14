from CharacterCreator import Creator
# Stwórz instancję Warrior
warrior = Creator.create("mage", 300)

print(f"Level: {warrior.level}, Strength: {warrior.ds}, Dexterity: {warrior.dz}, Intelligence: {warrior.di}")