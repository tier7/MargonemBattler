from character import Character

class Hunter(Character):
    def __init__(self, level):
        super().__init__(level)
        self.update_attributes()

    def update_attributes(self):
        for level in range(1, self.level + 1):
            if level < 21:
                self.ds+=1
                self.dz+=4
            else:
                self.dz+=5