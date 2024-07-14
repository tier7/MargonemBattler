from character import Character

class Tracker(Character):
    def __init__(self, level):
        super().__init__(level)
        self.update_attributes()

    def update_attributes(self):
        for level in range(1, self.level + 1):
            if level < 21:
                self.di += 2
                self.ds += 1
                self.dz += 2
            else:
                if level%2 == 0:
                    self.di += 3
                    self.dz += 2
                else:
                    self.di += 2
                    self.dz += 3