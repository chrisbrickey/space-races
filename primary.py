from home import home_start, ending
from planets import Planet, planet_list
from puzzles import puzzles


def game_engine (trip_counter):

    while trip_counter <= 1:
        trip_output = atlas(trip_counter)
        trip_counter += 1

    if  int(trip_output) >= 100:
        end_status = "won"
    elif int(trip_output) < 100:
        end_status = "lost"
    else:
        pass

    ending(player_name, end_status)


def atlas (trip_counter):

    if trip_counter == 0:
        home_start(player_name)
        return "leaving home"

    elif trip_counter == 1:
        print "\nYou've been given a map with %s potential planets on it." % (len(planet_list))
        print "You only have enough fuel to travel to one of those planets."
        print "Below is a list of the puzzles you have to solve to get the coordinates of each planet.\n"

        #in subsequent versions, pull from planet_list instead of hard coded
        print """
            planet1: guess-a-number
            planet2: meteorite-laser-reflector
            planet3: deal-me-in
            """

        selected_planet_name = raw_input("\nType the name of the planet you want to explore (e.g. planet3): ")

        puzzles(selected_planet_name)

        for planet in planet_list:
            if planet._name == selected_planet_name:
                selected_planet = planet
                break

        selected_planet.travel()

        selected_planet.test()

        return selected_planet.analyze()

    else:
        pass


player_name = raw_input("Please type your name: ")
trip_counter = 0
game_engine(trip_counter)
