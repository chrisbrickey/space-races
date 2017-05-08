def home_start (player_name):
    print "\nWelcome to Space Race, " + player_name + "!"
    print "Earth's environment is quickly deteriorating."
    print "Your mission is to find a planet that is suitable for relocation of friendly humans."

def ending (player_name, end_status):

    if end_status == "won":
        print "\nYOU WON SPACE RACE!!"
        print "You found a suitable planet for humans."
        print player_name + " returns home in victory.\n"
        exit()
    elif end_status == "lost":
        print "\nGAME OVER, " + player_name + "."
        print "This planet isn't suitable and you don't have enough fuel to visit any more planets."
        print "You must return to your home planet to refuel before playing again.\n"
        exit()
    else:
        print "\nend_status still isn't working\n"
        print end_status
        exit()
