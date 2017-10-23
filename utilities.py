def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def end_game(player_name, end_status):

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
