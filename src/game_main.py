game_state = "menu"

def startgame():
    while True:
        match game_state:
            case "menu":
                print("cool menu")

            case _:
                print("error: impossible game state")
