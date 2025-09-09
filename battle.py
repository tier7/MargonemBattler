import effects
import character

from professions.paladin import Paladin
from professions.warrior import Warrior
from professions.hunter import Hunter
from professions.mage import Mage
from professions.tracker import Tracker
from professions.bladeDancer import BladeDancer

class Battle():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    # default actions

    basic_attack = 0        # atak podstawowy (bez many, energii)

    def getPos(self, profession):

        # first lane

        if profession == "paladin" or "warrior" or "bladeDancer":
            return Paladin.position # the same position (all)

        # second lane

        if profession == "mage":
            return Mage.position

        # third lane

        if profession == "tracker" or "hunter":
            return Tracker.position # the same position

    def isAble(self, profession):
        if profession == "paladin" or "warrior" or "bladeDancer":
            return Paladin.able_to_walk

        if profession == "mage":
            return Mage.able_to_walk

        if profession == "tracker" or "hunter":
            return Tracker.able_to_walk

    def count_of_steps(self, player1, player2, profession):
        step_forward = 0        # krok do przodu

        if player1.isAble and player2.isAble:
            return

        if not player1.isAble and not player2.isAble:
            return

        if player1.isAble(profession):
            if not player2.isAble(profession):
                step_forward = player2.getPos - player1.getPos
        elif player2.isAble(profession):
            if not player1.isAble(profession):
                step_forward = player1.getPos - player2.getPos

        return step_forward

    def battle(self):
        round_count = 0
        player1_at_sum = 0
        player2_at_sum = 0
        while round_count < 10:
            player1_at = effects.Effects.calculate_final_AT(self.player1,self.player2)
            player2_at = effects.Effects.calculate_final_AT(self.player2,self.player1)
            if player1_at_sum + player1_at < player2_at_sum + player2_at:
                self.player1.attack(self.player2)
                print("gracz 1 wykonal ruch")
                player1_at_sum += player1_at
            else:
                self.player2.attack(self.player1)
                print("gracz 2 wykonal ruch")
                player2_at_sum += player2_at
            round_count +=1