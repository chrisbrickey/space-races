import random
from utilities import is_int

class PuzzleSelector (object):

    def __init__(self, puzzle_name):
        self.puzzle_name = puzzle_name

    def run_puzzle(self):

        if self.puzzle_name == "guess-a-number":
            new_puzzle = GuessNumberPuzzle()
        elif self.puzzle_name ==  "meteorite-laser-reflector":
            new_puzzle = MLRPuzzle()
        elif self.puzzle_name == "deal-me-in":
            new_puzzle = BlackjackPuzzle()
        else:
            pass

        new_puzzle.print_intro()
        result = new_puzzle.play()
        return result


class GuessNumberPuzzle (object):

    bounds = [1, 100]

    def print_intro(self):
        print("""
            The computer will select an integer at random between 1 and 100 (inclusive).\n
            You have 10 chances to guess the number.\n
            If you don't guess correctly by the tenth chance, the game ends.\n
            """)

    def play(self):
        secret_number = random.randint(*GuessNumberPuzzle.bounds)

        puzzle_counter = 1
        while puzzle_counter <= 10:

            user_guess = input("\nType an integer between %s and %s (inclusive): " % (GuessNumberPuzzle.bounds[0], GuessNumberPuzzle.bounds[1]))
            while (is_int(user_guess) == False) or (int(user_guess) not in range (GuessNumberPuzzle.bounds[0], (GuessNumberPuzzle.bounds[1] + 1))):
                user_guess = input("\nThat's out of range. Type an integer between %s and %s (inclusive): " % (GuessNumberPuzzle.bounds[0], GuessNumberPuzzle.bounds[1]))

            user_guess = int(user_guess)

            if puzzle_counter == 10:
                if (user_guess < secret_number):
                    print("That was your tenth and final valid guess. It was too low.\n\n")
                    return "not success"
                elif (user_guess > secret_number):
                    print("That was your tenth and final valid guess. It was too high.\n\n")
                    return "not success"
                else:
                    pass

            elif user_guess == secret_number:
                print("You guessed correctly! COORDINATES UNLOCKED\n\n")
                return "success"
            elif (user_guess < secret_number):
                print("Your guess is low. %s guesses remaining. Try again!" % (10 - puzzle_counter))
            elif (user_guess > secret_number):
                print("Your guess is high. %s guesses remaining. Try again!" % (10 - puzzle_counter))
            else:
                pass

            puzzle_counter += 1


class MLRPuzzle (object):

    mlr_choices = ["meteorite", "laser", "reflector"]

    #read this like....Does meteorite beat laser?...No, YOU LOSE
    mlr_outcome_table = {
        "mm": "It's a DRAW",
        "ml": "Laser destroys meteorite. \nYOU LOSE.\n\n",
        "mr": "Meteorite crushes reflector. \nYOU WIN! Coordinates unlocked.\n\n",
        "lm": "Laser destroys meteorite. \nYOU WIN! Coordinates unlocked.\n\n",
        "ll": "It's a DRAW",
        "lr": "Reflector deflects laser. \nYOU LOSE.\n\n",
        "rm": "Meteorite crushes reflector. \nYOU LOSE.\n\n",
        "rl": "Reflector deflects laser. \nYOU WIN! Coordinates unlocked.\n\n",
        "rr": "It's a DRAW"
    }

    def print_intro(self):
        print("""
            This puzzle works like rock/paper/scissors.\n
            The computer will choose a weapon and you will choose a weapon.\n
            If your weapon beats the computer's weapon, you win.\n
            You only get three chances. If you don't win by the third chance, the game ends.\n
            """)

    def play(self):
        puzzle_counter = 0
        while puzzle_counter < 3:

            print("\n\t----- Playing round %d of %d -----" % ((puzzle_counter + 1), len(MLRPuzzle.mlr_choices)))

            computer_choice = MLRPuzzle.mlr_choices[random.randint(0, (len(MLRPuzzle.mlr_choices) - 1))]

            user_choice = input("\nSelect your weapon by typing 'meteorite', 'laser', or 'reflector': ")
            while user_choice not in MLRPuzzle.mlr_choices:
                user_choice = input("\nThat's not a meteorite, laser, or reflector. Try again: ")

            print("\nYou chose: %s" % user_choice)
            print("Computer chose: %s" % computer_choice)
            matchup = user_choice.split()[0][0] + computer_choice.split()[0][0]
            print("\n%s\n" % MLRPuzzle.mlr_outcome_table[matchup])

            if (matchup == "lm") or (matchup == "rl") or (matchup == "mr"):
                return "success"
            else:
                if puzzle_counter == 2:
                    print("\nThat was the third round - your last chance within this puzzle.\n\n")
                    return "not success"
                else:
                    puzzle_counter += 1


class BlackjackPuzzle (object):

    #keys = numeric representation; values = [name of card, point vBlackjackalue]
    blackjack_table = {
        2: ["two", 2],
        3: ["three", 3],
        4: ["four", 4],
        5: ["five", 5],
        6: ["six", 6],
        7: ["seven", 7],
        8: ["eight", 8],
        9: ["nine", 9],
        10: ["ten", 10],
        11: ["jack", 10],
        12: ["queen", 10],
        13: ["king", 10],
        14: ["ace", 11]
    }

    bounds = [2, 14]

    def draw_random_card(self):
        return random.randint(*BlackjackPuzzle.bounds)

    def print_intro(self):
        print("""
            This puzzle is similar to blackjack with many exceptions:\n
            \t* 16 is the magic number. When your cards sum to 16,YOU automatically win. Exceeding 16 is BUST.\n
            \t* All cards are drawn at random. Ignore the odds of a real deck of cards.\n
            \t* Aces are always 11 points.\n\n

            Card values:\n
            \t* Ace = 11 points\n
            \t* Jack = Queen = King = 10 points\n
            \t* Point-cards are taken at face value: 'six' = 6 points\n\n

            Playing the game:\n
            \t* Computer is dealer. The dealer always gets two cards.\n
            \t* You will be dealt one card. Then can decide whether or not you want to 'hit' to get a second card.\n\n

            Winning the game:
            \t* To win, the sum of your card(s) must be >= the dealer's sum without exceeding 16.\n
            \t* You must win one of the three rounds to unlock this planet's coordinates.\n\n
            """)


    def play(self):
        puzzle_counter = 0
        while puzzle_counter < 3:

            print("\n\t----- Playing round %d of 3 -----\n" % (puzzle_counter + 1))
            dealer_card1 = self.draw_random_card()
            dealer_card2 = self.draw_random_card()
            dealer_sum = (BlackjackPuzzle.blackjack_table[dealer_card1][1]) + (BlackjackPuzzle.blackjack_table[dealer_card2][1])

            player_card1 = self.draw_random_card()
            player_card2 = self.draw_random_card()

            print("DEALER has a(n) %s." % BlackjackPuzzle.blackjack_table[dealer_card1][0])
            print("YOU have a(n) %s." % BlackjackPuzzle.blackjack_table[player_card1][0])
            command = input("\n\nType 'stand' to play with only one card. Type 'hit' to get a second card: ")
            while command not in ["stand", "hit"]:
                command = input("\nThat's not 'stand' or 'hit'. Try again: ")

            print("\nDEALER'S second card is a(n) %s" % BlackjackPuzzle.blackjack_table[dealer_card2][0])
            print("So DEALER'S sum is %s" % dealer_sum)

            if command == "stand":
                player_sum = BlackjackPuzzle.blackjack_table[player_card1][1]
                print("YOUR single card is worth " + str(player_sum) + " points.")
            elif command == "hit":
                print("\nYOUR second card is a(n) " + str(BlackjackPuzzle.blackjack_table[player_card2][0]) + ".")
                player_sum = (BlackjackPuzzle.blackjack_table[player_card1][1]) + (BlackjackPuzzle.blackjack_table[player_card2][1])
            else:
                pass

            print("So YOUR sum is %s" % player_sum)


            if puzzle_counter == 2:

                if player_sum == 16:
                    print("\nYou got a SWEET SIXTEEN! Coordinates unlocked immediately!\n\n")
                    return "success"
                elif player_sum > 16:
                    print("\nYou're over 16. BUST!\n\n")
                    return "not success"
                elif (player_sum >= dealer_sum) or (dealer_sum > 16):
                    print("\nYOU WIN! Coordinates unlocked.\n\n")
                    return "success"
                else:
                    print("\nDEALER wins.")
                    return "not success"

            elif player_sum == 16:
                print("\nYou got a SWEET SIXTEEN! Coordinates unlocked immediately!\n\n")
                return "success"
            elif player_sum > 16:
                print("\nYou're over 16. BUST!\n\n")
            elif (player_sum >= dealer_sum) or (dealer_sum > 16):
                print("\nYOU WIN! Coordinates unlocked.\n\n")
                return "success"
            else:
                print("\nDEALER wins.")

            puzzle_counter += 1
