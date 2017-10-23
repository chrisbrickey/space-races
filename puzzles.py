# Next steps:  Break out intro printing into separate methods

import random
from utilities import is_int


class GuessNumberPuzzle (object):

    bounds = [1, 100]

    def play_guess_number(self):
        print """
            The computer will select an integer at random between 1 and 100 (inclusive).\n
            You have 10 chances to guess the number.\n
            If you don't guess correctly by the tenth chance, the game ends.\n
            """

        secret_number = random.randint(*GuessNumberPuzzle.bounds)

        puzzle_counter = 1
        while puzzle_counter <= 10:

            user_guess = raw_input("\nType an integer between %s and %s (inclusive): " % (GuessNumberPuzzle.bounds[0], GuessNumberPuzzle.bounds[1]))
            while (is_int(user_guess) == False) or (int(user_guess) not in range (GuessNumberPuzzle.bounds[0], (GuessNumberPuzzle.bounds[1] + 1))):
                user_guess = raw_input("\nThat's out of range. Type an integer between %s and %s (inclusive): " % (GuessNumberPuzzle.bounds[0], GuessNumberPuzzle.bounds[1]))

            user_guess = int(user_guess)

            if puzzle_counter == 10:
                if (user_guess < secret_number):
                    print "That was your tenth and final valid guess. It was too low.\n\n"
                    return "not success"
                elif (user_guess > secret_number):
                    print "That was your tenth and final valid guess. It was too high.\n\n"
                    return "not success"
                else:
                    pass

            elif user_guess == secret_number:
                print "You guessed correctly! COORDINATES UNLOCKED\n\n"
                return "success"
            elif (user_guess < secret_number):
                print "Your guess is low. %s guesses remaining. Try again!" % (10 - puzzle_counter)
            elif (user_guess > secret_number):
                print "Your guess is high. %s guesses remaining. Try again!" % (10 - puzzle_counter)
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

    def play_metorite_laser_reflector(self):
        print """
            This puzzle works like rock/paper/scissors.\n
            The computer will choose a weapon and you will choose a weapon.\n
            If your weapon beats the computer's weapon, you win.\n
            You only get three chances. If you don't win by the third chance, the game ends.\n
            """

        puzzle_counter = 0
        while puzzle_counter < 3:

            print "\n\t----- Playing round %d of %d -----" % ((puzzle_counter + 1), len(MLRPuzzle.mlr_choices))

            computer_choice = MLRPuzzle.mlr_choices[random.randint(0, (len(MLRPuzzle.mlr_choices) - 1))]

            user_choice = raw_input("\nSelect your weapon by typing 'meteorite', 'laser', or 'reflector': ")
            while user_choice not in MLRPuzzle.mlr_choices:
                user_choice = raw_input("\nThat's not a meteorite, laser, or reflector. Try again: ")

            print "\nYou chose: %s" % user_choice
            print "Computer chose: %s" % computer_choice
            matchup = user_choice.split()[0][0] + computer_choice.split()[0][0]
            print "\n%s\n" % MLRPuzzle.mlr_outcome_table[matchup]

            if (matchup == "lm") or (matchup == "rl") or (matchup == "mr"):
                return "success"
            else:
                if puzzle_counter == 2:
                    print "\nThat was the third round - your last chance within this puzzle.\n\n"
                    return "not success"
                else:
                    puzzle_counter += 1



class Puzzle (object):

    #keys = numeric representation; values = [name of card, point value]
    blackjack_table = {
        1: ["one", 1],
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


    def __init__(self, puzzle_name):
        self.puzzle_name = puzzle_name


    def run_puzzle(self):
        result = None
        if self.puzzle_name == "guess-a-number":
            new_puzzle = GuessNumberPuzzle()
            result = new_puzzle.play_guess_number()
        elif self.puzzle_name ==  "meteorite-laser-reflector":
            new_puzzle = MLRPuzzle()
            result = new_puzzle.play_metorite_laser_reflector()
        elif self.puzzle_name == "deal-me-in":
            result = self.play_deal_me_in()
        else:
            pass

        return result


    def play_deal_me_in(self):
        print """
            This is similar to blackjack but 16 is the magic number and each draw is random (neglect the odds in a real deck of cards).\n
            \nPoint-cards are taken at face value:'six' = 6 points\n
            Jack = Queen = King = 10 points\n
            Ace = 11 points\n
            \nThe computer is the dealer. You will only see your first card and the dealer's first card.\n
            You get to decide whether or not you want to 'stand' with one card or 'hit' to get a second card.\n
            The dealer always gets two cards.\n
            To win, the sum value of your card(s) must be equal to or greater than the dealer's sum value without exceeding 16.\n
            \nYou only get three chances to win before the game ends.\n
            """

        puzzle_counter = 0
        while puzzle_counter < 3:

            print "\n\t----- Playing round # %d -----\n" % (puzzle_counter + 1)
            dealer_card1 = random.randint(1, 14)
            dealer_card2 = random.randint(1, 14)
            dealer_sum = (Puzzle.blackjack_table[dealer_card1][1]) + (Puzzle.blackjack_table[dealer_card2][1])

            player_card1 = random.randint(1, 14)
            player_card2 = random.randint(1, 14)

            print "The dealer has a(n) %s." % Puzzle.blackjack_table[dealer_card1][0]
            print "You have a(n) %s." % Puzzle.blackjack_table[player_card1][0]
            command = raw_input("\n\nType 'stand' to play with only one card. Type 'hit' to get a second card: ")
            while command not in ["stand", "hit"]:
                command = raw_input("\nThat's not 'stand' or 'hit'. Try again: ")

            if command == "stand":
                player_sum = Puzzle.blackjack_table[player_card1][1]
                print "Your single card is worth " + str(player_sum) + " points."
            elif command == "hit":
                print "\nYour second card is a(n) " + str(Puzzle.blackjack_table[player_card2][0]) + "."
                player_sum = (Puzzle.blackjack_table[player_card1][1]) + (Puzzle.blackjack_table[player_card2][1])
            else:
                pass

            print "The sum value of your card(s): %s" % player_sum
            print "\nThe dealer's second card is a(n) %s" % Puzzle.blackjack_table[dealer_card2][0]
            print "So the dealer's sum value is: %s" % dealer_sum

            if puzzle_counter == 2:

                if player_sum == 16:
                    print "\nYou got a SWEET SIXTEEN! Coordinates unlocked immediately!\n\n"
                    return "success"
                elif player_sum > 16:
                    print "\nYou're over 21. BUST!\n\n"
                    return "not success"
                elif (player_sum >= dealer_sum) or (dealer_sum > 16):
                    print "\nYOU WIN! Coordinates unlocked.\n\n"
                    return "success"
                else:
                    print "\nDealer wins."
                    return "not success"

            elif player_sum == 16:
                print "\nYou got a SWEET SIXTEEN! Coordinates unlocked immediately!\n\n"
                return "success"
            elif player_sum > 16:
                print "\nYou're over 21. BUST!\n\n"
            elif (player_sum >= dealer_sum) or (dealer_sum > 16):
                print "\nYOU WIN! Coordinates unlocked.\n\n"
                return "success"
            else:
                print "\nDealer wins."

            puzzle_counter += 1
