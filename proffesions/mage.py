from character import Character

class Mage(Character):
    def __init__(self, level):
        super().__init__(level)
        self.update_attributes()

    def update_attributes(self):
        for level in range(1, self.level + 1):
            if level < 21:
                self.di += 3
                self.ds += 1
                self.dz += 1
            else:
                self.dz += 5
