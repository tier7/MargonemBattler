import effects
import character
class Battle():
    def __init__(self,player1 ,player2):
        self.player1 = player1
        self.player2 = player2


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