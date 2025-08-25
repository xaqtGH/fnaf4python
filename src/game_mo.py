# Movement opportunities are what allows most animatronics to move.
# They vary from one animatronic to another, but the concept largely stays the same:
# it affects Bonnie, Foxy, Chica, and Fredbear the most based on a timer
# AI Level determines the frequency of these movement opportunities

import random, math, time

def MovementOpportunity(animatronic):
    match MovementOpportunity(animatronic):
        case MovementOpportunity(Bonnie):
            time.sleep(3)
            BonnieMORoll = random.randint(BonnieAI, 20)
            
            if InFarLeftHall == True:
                
