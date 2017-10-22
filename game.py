from home import start, end
from planets import Planet, planet_list, planets
from puzzles import Puzzle


puzzle_list = ["guess-a-number", "meteorite-laser-reflector", "deal-me-in"]
planet_count = len(planets)
#
# planet_list = [
#     Planet("planet1", "guess-a-number", 17, 25, 19, 23),
#     Planet("planet2", "meteorite-laser-reflector", 31, 27, 14, 35),
#     Planet("planet3", "deal-me-in", 21, 18, 12, 37)
#     ]

class Game (object):

    def __init__(self, player_name):
        self.player_name = player_name
        self.planets_visited = []
        self.trip_counter = 0
        self.puzzle_count = 0


    def play(self):
        start(self.player_name)

        while self.puzzle_count <= 3:
            print "puzzle_count: %s" % self.puzzle_count

            if self.puzzle_count == 3:
                print """
                    You have exhausted your 3 attempts to find coordinates.\n
                    Please play again.
                    """
                exit()
            else:
                puzzle_result = self.get_coordinates()
                if puzzle_result == "success":
                    print "im in the success fork===================================="
                    break
                else:
                    self.puzzle_count += 1


        while self.trip_counter < 1:
            trip_output = self.travel_to_planet()
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
    def get_coordinates(self):
        print "You have attempted %s puzzle(s). You have %s attempt(s) remaining." % (self.puzzle_count, (3 - self.puzzle_count))
        print "Below is a list of the planets and the puzzles you must solve to get the coordinates of each planet.\n"

        for index in range(planet_count):
            print "%s) %s: %s" % ((index + 1), planets[index], puzzle_list[index])

        selected_number = raw_input("\nType the number of the planet you wish to attempt (1, 2, etc.): ")
        while (is_int(user_guess) == False) or (  int(selected_number) not in range(1, (planet_count + 1))):
            selected_number = raw_input("\nThat's out of range. Try again: ")

        planet_puzzle_index = int(selected_number) - 1
        selected_planet_name = planets[planet_puzzle_index]
        selected_puzzle_name = puzzle_list[planet_puzzle_index]

        print "\n\t----- INSTRUCTIONS TO UNLOCK COORDINATES OF %s -----" % selected_planet_name.upper()

        new_puzzle = Puzzle(selected_puzzle_name)
        return new_puzzle.run_puzzle()


    def travel_to_planet(self):
        for planet in planet_list:
            if planet._name == selected_planet_name:
                selected_planet = planet
                break

        selected_planet.travel()
        selected_planet.test()
        return selected_planet.analyze()




if __name__ == "__main__":
    player_name = raw_input("What's your name? ")
    game = Game(player_name)
    game.play()
