planets = ["planet1", "planet2", "planet3"]
# planet_list = [
#     Planet("planet1", "guess-a-number", 17, 25, 19, 23),
#     Planet("planet2", "meteorite-laser-reflector", 31, 27, 14, 35),
#     Planet("planet3", "deal-me-in", 21, 18, 12, 37)
#     ]

class Planet (object):

    def __init__(self, planet_name, puzzle_name, air, water, soil, inhabitants):
        self._name = planet_name
        self._puzzle = puzzle_name
        self._air = air
        self._water = water
        self._soil = soil
        self._inhabitants = inhabitants


    def travel (self):
        #print "Puzzles are not yet loaded so we assume you passed the quiz for " + str(self._name) + "."
        print "\nGreat job! The coordinates for " + str(self._name) + " are being loaded to your ship."
        print "Hang on! You're about to travel at warp speed to " + str(self._name) + "."
        print "\n\t----- a few hours later -----\n"
        print "You've landed safely on the surface of " + str(self._name) + "."
        print "Now you need to perform some tests to determine if this is a suitable planet."


    def test(self):

        authorization = raw_input("\nInitialize tests by typing GO here: ")

        if authorization == "GO":
            print "\nTest results for " + str(self._name) + "..."
            print "Air Quality: " + str(self._air)
            print "Water Quality: " + str(self._water)
            print "Soil Nutrients: " + str(self._soil)
            print "Inhabitant Friendliness: " + str(self._inhabitants)
        else:
            print "Authorization Error: Please make sure you typed GO."


    def analyze(self):

        print "\nIn order for the planet to be suitable for humans, the sum of these scores must be at least 100."
        authorization2 = raw_input("\nInterpret the results by typing GO here: ")

        if authorization2 == "GO":
            sum_of_results = self._air + self._water + self._soil + self._inhabitants
            print "\nThe sum is: " + str(sum_of_results)
        else:
            sum_of_results = "N/A"
            print "\nAuthorization Error: Please make sure you typed GO."

        return sum_of_results


planet_list = [
    Planet("planet1", "guess-a-number", 17, 25, 19, 23),
    Planet("planet2", "meteorite-laser-reflector", 31, 27, 14, 35),
    Planet("planet3", "deal-me-in", 21, 18, 12, 37)
    ]

#-----below code isfor testing when running this file only-----
#selected_planet_name = raw_input("\nType the name of the planet you want to try: ")

#for planet in planet_list:
#    if planet._name == selected_planet_name:
#        selected_planet = planet
#        break
#selected_planet.travel()
