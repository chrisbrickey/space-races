from home import home_start, ending
from planets import Planet
from planets import planet_list
from puzzles import puzzles

planets = ["planet1", "planet2", "planet3"]
puzzle_list = ["guess-a-number", "meteorite-laser-reflector", "deal-me-in"]


def game_engine (trip_counter):

    while trip_counter <= 1:
        trip_output = map(trip_counter)
        trip_counter += 1

    if  int(trip_output) >= 100:
        end_status = "won"
    elif int(trip_output) < 100:
        end_status = "lost"
    else:
        pass

    ending(player_name, end_status)


def map (trip_counter):

    if trip_counter == 0:
        home_start(player_name)
        return "leaving home"

    elif trip_counter == 1:
        print "\n%s potential planets have been identified." % (len(planets))
        print "You only have enough fuel to travel to 1 of those planets."
        print "Below is a list of the planets and the puzzles you have to solve to get the coordinates of each planet.\n"

        for index in range(len(planets)):
            print "%s: %s" % (planets[index], puzzle_list[index])

        selected_planet_name = raw_input("\nWhich planet would you like to visit? ")
        while selected_planet_name not in planets:
            selected_planet_name = raw_input("\nThat's not a real planet. Try again: ")

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


player_name = raw_input("What's your name? ")
trip_counter = 0
game_engine(trip_counter)
