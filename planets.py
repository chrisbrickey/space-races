class Planet (object):

    def __init__(self, planet_name, air, water, soil, inhabitants):
        self._name = planet_name
        self._air = air
        self._water = water
        self._soil = soil
        self._inhabitants = inhabitants


    def travel (self):
        print("\nGreat job! The coordinates for " + str(self._name) + " are being loaded to your ship.")
        print("Hang on! You're about to travel at warp speed to " + str(self._name) + ".")
        print("\n\t----- a few hours later -----\n")
        print("You've landed safely on the surface of " + str(self._name) + ".")
        print("Now you need to perform some tests to determine if this is a suitable planet.")


    def test(self):
        authorization = input("\nInitialize tests by typing GO here: ")
        while authorization not in ["GO", "go", "Go", "gO"]:
            authorization = input("\nThat doesn't make sense. Please type 'GO': ")

        print("\nTest results for " + str(self._name) + "...")
        print("Air Quality: " + str(self._air))
        print("Water Quality: " + str(self._water))
        print("Soil Nutrients: " + str(self._soil))
        print("Inhabitant Friendliness: " + str(self._inhabitants))


    def analyze(self):
        print("\nIn order for the planet to be suitable for humans, the sum of these scores must be at least 100.")
        authorization2 = input("\nInterpret the results by typing GO here: ")
        while authorization2 not in ["GO", "go", "Go", "gO"]:
            authorization2 = input("\nThat doesn't make sense. Please type 'GO': ")

        sum_of_results = self._air + self._water + self._soil + self._inhabitants
        print("\nThe sum is: " + str(sum_of_results))
        return sum_of_results
