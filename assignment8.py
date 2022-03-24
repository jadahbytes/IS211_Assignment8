import random
import time

random.seed(0)


class Die:
    def __init__(self, sides=6):
        self.sides = sides
        self.roll()

    def roll(self):
        return random.randint(1, self.sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.die = Die()

    def turn(self):
        turn_total = 0
        choice = 'r'
        while choice == 'r':
            roll = self.die.roll()
            if roll != 1:
                print(f"{self.name} rolled {roll}.")
                turn_total = turn_total + roll
                print(f"- {self.name} | Turn total {turn_total} -")
                choice = input('- Enter "r" to roll or "h" to hold. -').lower()
            else:
                print(f"{self.name} rolled a 1. End turn :(")
                turn_total = 0
                choice = 'h'
        self.total += turn_total
        print(f"{self.name}'s turn is over.")
        print(f"{self.name} | Game total: {self.total}")
        print("-------------------------------------------------------")


class ComputerPlayer(Player):
    def turn(self):
        turn_total = 0
        choice = 'r'
        while choice == 'r':
            roll = self.die.roll()
            if roll != 1:
                print(f'{self.name} rolled a {roll}')
                turn_total = turn_total + roll
                print(f"-{self.name} | Turn total {turn_total}-")
                if turn_total < (25 if 25 < (100 - self.total) else (100 - self.total)):
                    print(f"{self.name} rolls again.")
                else:
                    choice = 'h'
            else:
                print(f"{self.name} rolled a 1. End of turn :(")
                turn_total = 0
                choice = 'h'
        self.total += turn_total
        print(f"{self.name}'s turn is over.")
        print(f"{self.name} | Turn total: {turn_total} | Game total: {self.total}")
        print("-------------------------------------------------------")


class Game:
    def __init__(self):
        players = Factory()
        self.player1 = players.player1
        self.player2 = players.player2
        self.die = Die()

    def play(self):
        while self.player1.total < 100 and self.player2.total < 100:
            self.player1.turn()
            if self.player1.total < 100:
                self.player2.turn()
        if self.player1.total > self.player2.total:
            print(f'''
            ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===>
            {self.player1.name} is the winner!
            ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===>''')
        else:
            print(f'''
            ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===>
            {self.player2.name} is the winner!
            ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===>''')


class Factory:
    def __init__(self):
        print("Enter '1' to play a human player. Enter '2' to play a computer player. Enter '3' for two computer "
              "players.")
        try:
            option = int(input())
            if option == 1:
                self.player1 = Player("Human One")
                self.player2 = Player("Human Two")
            elif option == 2:
                self.player1 = Player("Human Player")
                self.player2 = ComputerPlayer("Computer Player")
            elif option == 3:
                self.player1 = ComputerPlayer("Computer One")
                self.player2 = ComputerPlayer("Computer Two")

            else:
                print("Invalid entry. Enter '1' to play a human player. Enter '2' to play a computer player. "
                      "Enter '3' for two computer players.")
        except:
            print("Invalid entry. Enter '1' to play a human player. Enter '2' to play a computer player. Enter '3' for "
                  "two computer players.")


class TimedGameProxy:
    def __init__(self):
        self.die = Die()
        players = Factory()
        self.player1 = players.player1
        self.player2 = players.player2

    def play(self):
        start_time = time.time()
        while self.player1.total < 100 and self.player2.total < 100:
            end_time = time.time()
            if (end_time - start_time) < 60:
                self.player1.turn()
                if self.player1.total < 100:
                    end_time = time.time()
                    if (end_time - start_time) < 60:
                        self.player2.turn()
                    else:
                        print('One minute has passed.')
                        break
                else:
                    print('One minute has passed.')
                    break
            if self.player1.total > self.player2.total:
                print(f'{self.player1.name} wins!')
            else:
                print(f'{self.player2.name} wins!')


if __name__ == '__main__':

    print('''Welcome to the game of Pig
─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄
█░░░█░░░░░░░░░░▄▄░██░█
█░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█
█░░░▀░░░▄▄▄▄▄░░██░▀▀░█
─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀
''')

    game = Game()
    game.play()
