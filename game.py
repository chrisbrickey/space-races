from home import start, end
from planets import Planet, planet_list
from puzzles import Puzzle

planets = ["planet1", "planet2", "planet3"]
puzzle_list = ["guess-a-number", "meteorite-laser-reflector", "deal-me-in"]
#
# planet_list = [
#     Planet("planet1", "guess-a-number", 17, 25, 19, 23),
#     Planet("planet2", "meteorite-laser-reflector", 31, 27, 14, 35),
#     Planet("planet3", "deal-me-in", 21, 18, 12, 37)
#     ]

class Game (object):

    def __init__(self, player_name):
        self.player_name = player_name
        self.trip_counter = 0


    def play(self):
        start(self.player_name)

        while self.trip_counter <= 1:
            trip_output = self.game_map()
            self.trip_counter += 1

        #rewrite so that user can visit 2 planets instead of just one
        if  int(trip_output) >= 100:
            end_status = "won"
        elif int(trip_output) < 100:
            end_status = "lost"
        else:
            pass

        end(self.player_name, end_status)


    #instance methods do not need to be coded above the line where they are called; that is not the case for functions (outside of classes)
    def game_map(self):
        print "\n%s potential planets have been identified." % (len(planets))
        print "You only have enough fuel to travel to 1 of those planets, but first you must solve puzzles to get the coordinates of planet."

        coordinate_attempts = []


        #rewrite so that user can visit 2 planets instead of just one
        if self.trip_counter == 0:
            print "You have attempted %s puzzles. So you can selec"
            print "Below is a list of the planets and the puzzles you have to solve to get the coordinates of each planet.\n"

            for index in range(len(planets)):
                print "%s: %s" % (planets[index], puzzle_list[index])

            selected_planet_name = raw_input("\nWhich planet would you like to visit? ")
            while selected_planet_name not in planets:
                selected_planet_name = raw_input("\nThat's not a real planet. Try again: ")

            print "\n\t----- INSTRUCTIONS TO UNLOCK COORDINATES OF %s -----" % selected_planet_name.upper()

            coordinate_attempts.append(selected_planet_name)
            new_puzzle = Puzzle(selected_planet_name)
            new_puzzle.choose_puzzle()

            for planet in planet_list:
                if planet._name == selected_planet_name:
                    selected_planet = planet
                    break

            selected_planet.travel()

            selected_planet.test()

            return selected_planet.analyze()

        else:
            pass




if __name__ == "__main__":
    player_name = raw_input("What's your name? ")
    game = Game(player_name)
    game.play()
