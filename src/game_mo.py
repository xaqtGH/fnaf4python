# Movement opportunities are what allows most animatronics to move.
# They vary from one animatronic to another, but the concept largely stays the same:
# it affects Bonnie, Foxy, Chica, and Fredbear the most based on a timer
# AI Level determines the frequency of these movement opportunities

# wip

import random, math, time

def doormove(animatronic): # Closing doors on animatronics sends most of them back
    match doormove(animatronic):
        case doormove(bonnie): # Successfully blocking off Bonnie sends him back to the living room
            if InLeftHall == True and LDoorIsClosed == True and LDoorTimer >= 3:
                InLeftHall = False
                InLivingRoom = True
                LDoorTimer = 0

            if InLeftHall == True and LeftHallIsFlashed == True:
                jumpscare(bonnie)

            if BonnieAttackPatience >= 0 and PlayerLocation == Bedroom:
                jumpscare(bonnie)

        case doormove(chica): # Successfully blocking off Chica sends her back to the living room
            if InRightHall == True and RDoorIsClosed == True and RDoorTimer >= 3:
                InRightHall = False
                InLivingRoom = True
                RDoorTimer = 0

            if InRightHall == True and RightHallIsFlashed == True:
                jumpscare(chica)

            if ChicaAttackPatience >= 0 and PlayerLocation == Bedroom:
                jumpscare(chica)
                


def move(animatronic): # Movement trees of the animatronics
    match move(animatronic):
        case move(bonnie): # Goes from the living room, to the far left hall, then gets to the left door, and finally the bedroom if left unchecked
            if InLivingRoom == True:
                InLivingRoom == False
                InFarLeftHall = True
                
            if InFarLeftHall == True:
                InFarLeftHall = False
                InLeftHall = True

                

        case move(chica): # From the living room, she either goes to the kitchen, or far right hall. From the far right hall she then moves to the door, and then the bedroom if left unchecked
            if InLivingRoom == True:
                KitchenChance = random.randint(1, 2)
                
                if KitchenChance == 1:
                    InLivingRoom = False
                    InFarRightHall = True
                    KitchenChance = 0

                elif KitchenChance == 2: # kitchen.wav
                    InLivingRoom = False
                    InKitchen = True
                    KitchenChance = 0

            if InFarRightHall == True:
                InFarRightHall = False
                InRightHall = True

        case move(foxy): # He's quite the complicated fella
            if InLivingRoom == True:
                FoxyHallChoice = random.randint(1, 2)
                
                if FoxyHallChoice == 1:
                    InFarLeftHall = True

                elif FoxyHallChoice == 2:
                    InFarRightHall = True


def MovementOpportunity(animatronic):
    match MovementOpportunity(animatronic):

        case MovementOpportunity(bonnie):
            time.sleep(5)
            BonnieMORoll = random.randint(BonnieAI, 20)

            if BonnieMORoll == BonnieAI and LeftHallIsFlashed == False:
                move(bonnie)
            
            elif InLivingRoom == True and LeftHallIsFlashed == True: # Bonnie always fails MO's if the left hall is flashed while he's in the living room
                pass

        case MovementOpportunity(chica):
            time.sleep(5)
            ChicaMORoll = random.randint(ChicaAI, 20)

            if ChicaMORoll == ChicaAI and RightHallIsFlashed == False: 
                move(chica)

            elif InLivingRoom == True and RightHallIsFlashed == True: # Chica always fails MO's if the right hall is flashed while she's in the living room
                pass
                
        case MovementOpportunity(foxy):
            time.sleep(5)
            FoxyMORoll = random.randint(FoxyAI, 20)

            if FoxyMORoll == FoxyAI and InLivingRoom == True:
                move(foxy)

            if FoxyMORoll == FoxyAI and InRightHall == True and RightHallIsFlashed == False:
                move(foxy)

            if FoxyMORoll == FoxyAI and InLeftHall == True and LeftHallIsFlashed == False:
                move(foxy)

            if FoxyMORoll == FoxyMORoll and InLeftHall == True and PlayerLocation == RightHall:
                move(foxy)

            if FoxyMORoll == FoxyMORoll and InRightHall == True and PlayerLocation == LeftHall:
                move(foxy)

