from character import Character

class BladeDancer(Character):
    def __init__(self, level):
        super().__init__(level)
        self.update_attributes()

    def update_attributes(self):
        for level in range(1, self.level + 1):
            if level < 21:
                self.ds+=3
                self.dz+=2
            else:
                if level%2 == 0:
                    self.ds+=2
                    self.dz+=3
                else:
                    self.ds += 3
                    self.dz += 2
