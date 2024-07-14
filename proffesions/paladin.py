from character import Character

class Paladin(Character):
    def __init__(self, level):
        super().__init__(level)
        self.update_attributes()

    def update_attributes(self):
        for level in range(1, self.level + 1):
            if level < 21:
                if level % 2 == 0:
                    self.ds += 2
                    self.di += 2
                    self.dz += 1
                else:
                    self.ds += 3
                    self.di += 2
            else:
                if level % 2 == 0:
                    self.ds += 2
                    self.di += 3
                else:
                    self.ds += 3
                    self.di += 2