# Next steps: Refactor so that other files use planet_attributes instead of planets array below
planets = ["planet1", "planet2", "planet3"]

planet_attributes = {
    0 : ["planet1", 17, 25, 19, 23],
    1 : ["planet2", 31, 27, 14, 35],
    2 : ["planet3", 21, 18, 12, 37]
    }


class Planet (object):

    def __init__(self, planet_name, air, water, soil, inhabitants):
        self._name = planet_name
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
