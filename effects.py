class Effects:
    @staticmethod
    def begin_AT(character):
        return (1/(character.sa+1))
    @staticmethod
    def SA_additive_modified(character):
        additive_modifiers_sum = 0
        return (character.sa + 1) * (1 + additive_modifiers_sum)

    @staticmethod
    def modifier_boost():
        return 0

    @staticmethod
    def slow_reduction():
        return 0

    @staticmethod
    def SA_constant_modifiers(character,opponent):
        if character.wasHit == True:
            weapon_modifier = int(max(opponent.weaponSlow.values()))
            eq_constant_modifiers_sum = int(opponent.slow)
        else:
            weapon_modifier = 0
            eq_constant_modifiers_sum = 0
        result = Effects.SA_additive_modified(character) - (weapon_modifier * (1 + Effects.modifier_boost() - Effects.slow_reduction()) +
                eq_constant_modifiers_sum * (1 - Effects.slow_reduction()))
        if result == 0:
            return 1
        else:
            return result

    @staticmethod
    def calculate_AT(character, opponent):
        at = min(1 / Effects.SA_constant_modifiers(character, opponent), 3 / (character.sa+1))
        return at

    @staticmethod
    def calculate_final_AT(character, opponent):
        effects = []
        sum = 1
        for i in effects:
            print(i)
            sum *= (1-i)
        return sum*Effects.calculate_AT(character,opponent)
