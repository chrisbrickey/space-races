# from home import start, end
from puzzles import Puzzle
from planets import Planet
from utilities import is_int, end_game


# Next steps: move these variables inside Game class
min_to_sustain_human_life = 100
planet_fuel_cost = 1000
starter_fuel_alottment = planet_fuel_cost
max_coordinate_attempts = 3
puzzle_list = ["guess-a-number", "meteorite-laser-reflector", "deal-me-in"]
planet_attributes = {
    0 : ["planet1", 17, 25, 19, 23], # sum = 84
    1 : ["planet2", 31, 27, 14, 35], # sum = 107
    2 : ["planet3", 21, 18, 12, 37] # sum = 88
    }
planet_count = len(planet_attributes)


class Game (object):

    def __init__(self, player_name):
        self.player_name = player_name
        self.fuel = starter_fuel_alottment
        self.puzzle_attempts = 0
        self.planets_visited = [] # collects indices after a puzzle is solved


    def greeting(self):
        print "\nWelcome to Space Race, %s!" % self.player_name
        print "Earth's environment is quickly deteriorating."
        print "Your mission is to find a planet that is suitable for relocation of friendly humans.\n"
        print "Our team identified %s potential planets for human habitation." % (planet_count)
        print "You have %s units of fuel. That is only enough to travel to %s of those planets.\n" % (self.fuel, (self.fuel / planet_fuel_cost))
        print "AND BEFORE YOU CAN TRAVEL, you must solve puzzles to get the coordinates of any planet.\n\n"


    def play(self):
        while self.puzzle_attempts <= max_coordinate_attempts:

            if self.puzzle_attempts == max_coordinate_attempts:
                print "\tYou have exhausted your %s attempts to find coordinates." % max_coordinate_attempts
                print "\tThe time to save humanity is expired.\n"
                print "\tGAME OVER"
                exit()
            else:
                result_status, planet_index = self.get_coordinates()
                if (result_status != "not success"): # puzzle was solved
                    self.planets_visited.append(planet_index)
                    break
                else:
                    self.puzzle_attempts += 1


        while (self.fuel > 0):  # fuel subtraction made immediately after puzzle is solved above
            trip_output = self.travel_to_planet(planet_index)
            self.fuel -= planet_fuel_cost

        #rewrite so that user can visit 2 planets instead of just one
        # end_status = None
        if  int(trip_output) >= min_to_sustain_human_life:
            end_status = "won"
        else:
            end_status = "lost"

        end_game(self.player_name, end_status)


    #instance methods do not need to be coded above the line where they are called; that is not the case for functions (outside of classes)
    def get_coordinates(self):
        print "You have attempted %s puzzle(s). You have %s attempt(s) remaining." % (self.puzzle_attempts, (max_coordinate_attempts - self.puzzle_attempts))
        print "Below is a list of the planets and the puzzles you must solve to get the coordinates of each planet.\n"

        for index in range(planet_count):
            print "%s) %s: %s" % ((index + 1), planet_attributes[index][0], puzzle_list[index])

        selected_number = raw_input("\nType the number of the planet you wish to attempt (1, 2, 3, etc.): ")
        while (is_int(selected_number) == False) or (  int(selected_number) not in range(1, (planet_count + 1))):
            selected_number = raw_input("\nThat's out of range. Try again: ")

        planet_puzzle_index = int(selected_number) - 1
        selected_planet_name = planet_attributes[planet_puzzle_index][0]
        selected_puzzle_name = puzzle_list[planet_puzzle_index]

        print "\n\t----- INSTRUCTIONS TO UNLOCK COORDINATES OF %s -----" % selected_planet_name.upper()

        # Next steps:  use index instead of puzzle name to choose and play puzzle
        new_puzzle = Puzzle(selected_puzzle_name)
        result = new_puzzle.run_puzzle()
        return [result, planet_puzzle_index]


    def travel_to_planet(self, planet_index):
        array_of_planet_attributes = planet_attributes[planet_index]
        selected_planet = Planet(*array_of_planet_attributes)

        selected_planet.travel()
        selected_planet.test()
        return selected_planet.analyze()




if __name__ == "__main__":
    player_name = raw_input("What's your name? ")
    game = Game(player_name)
    game.greeting()
    game.play()
