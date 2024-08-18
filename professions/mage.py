from character import Character

class Mage(Character):
    def __init__(self, level):
        super().__init__(level)
        self.update_attributes()
        self.position = 2
        self.able_to_walk = False
    def update_attributes(self):
        for level in range(2, self.level + 1):
            if level < 21:
                self.di += 3
                self.ds += 1
                self.dz += 1
            else:
                self.di += 5
