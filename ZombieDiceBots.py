print("Varun Bellad, 1AY24AI096, Sec-O")
# ZombieDiceBots.py

import random

DICE = {
    'green':  ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'],
    'yellow': ['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'],
    'red':    ['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun']
}

def roll_die(color):
    return random.choice(DICE[color])

def choose_dice_cup():
    # 6 green, 4 yellow, 3 red dice
    return ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3

class Bot:
    def __init__(self, name):
        self.name = name
        self.brains = 0
        self.shotguns = 0
        self.footsteps = 0

    def take_turn(self):
        print(f"\n{self.name}'s turn!")
        cup = choose_dice_cup()
        random.shuffle(cup)

        brains_this_turn = 0
        shotguns_this_turn = 0
        footsteps_dice = []

        while True:
            # Roll 3 dice (including footsteps dice carried over)
            dice_to_roll = footsteps_dice[:]
            footsteps_dice = []
            while len(dice_to_roll) < 3 and cup:
                dice_to_roll.append(cup.pop())

            if not dice_to_roll:
                print("No dice left to roll.")
                break

            print(f"Rolling dice: {dice_to_roll}")
            for die_color in dice_to_roll:
                result = roll_die(die_color)
                print(f"Rolled {die_color} die: {result}")

                if result == 'brain':
                    brains_this_turn += 1
                elif result == 'shotgun':
                    shotguns_this_turn += 1
                else:  # footsteps
                    footsteps_dice.append(die_color)

            print(f"Brains: {brains_this_turn}, Shotguns: {shotguns_this_turn}, Footsteps to reroll: {len(footsteps_dice)}")

            # Bot logic: stop if 2 or more shotguns or collected 3+ brains this turn
            if shotguns_this_turn >= 2:
                print(f"{self.name} got too many shotguns! Turn ends with no brains collected.")
                brains_this_turn = 0
                break
            elif brains_this_turn >= 3:
                print(f"{self.name} decides to stop and keep the brains.")
                break
            else:
                print(f"{self.name} continues rolling...")

        self.brains += brains_this_turn
        print(f"{self.name}'s total brains: {self.brains}")

def main():
    bots = [Bot("Bot 1"), Bot("Bot 2")]

    rounds = 5
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        for bot in bots:
            bot.take_turn()

    print("\nFinal scores:")
    for bot in bots:
        print(f"{bot.name}: {bot.brains} brains")

    winner = max(bots, key=lambda b: b.brains)
    print(f"\nWinner is {winner.name}!")

if __name__ == "__main__":
    main()
