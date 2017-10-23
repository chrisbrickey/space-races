def start(player_name, fuel, num_of_planets, cost_per_planet):
    print "\nWelcome to Space Race, %s!" % player_name
    print "Earth's environment is quickly deteriorating."
    print "Your mission is to find a planet that is suitable for relocation of friendly humans.\n"
    print "Our team identified %s potential planets for human habitation." % (num_of_planets)
    print "You have %s units of fuel. That is only enough to travel to %s of those planets.\n" % (fuel, (fuel / cost_per_planet))
    print "AND BEFORE YOU CAN TRAVEL, you must solve puzzles to get the coordinates of any planet.\n\n"

def end(player_name, end_status):

    if end_status == "won":
        print "\nYOU WON SPACE RACE!!"
        print "You found a suitable planet for humans."
        print "%s returns home in victory.\n" % player_name
        exit()
    elif end_status == "lost":
        print "\nGAME OVER, %s." % player_name
        print "This planet isn't suitable and you don't have enough fuel to visit any more planets."
        print "You must return to your home planet to refuel before playing again.\n"
        exit()
    else:
        pass
