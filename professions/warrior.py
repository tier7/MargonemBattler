from character import Character
class Warrior(Character):

    # static values
    position = 1
    able_to_walk = True

    def __init__(self, level):
        super().__init__(level)
        self.update_attributes()

    def update_attributes(self):
        for level in range(2, self.level + 1):
            if level < 21:
                self.ds += 4
                self.dz += 1
            else:
                self.ds += 5
