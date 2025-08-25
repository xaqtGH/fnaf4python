#tmp file
import pygame
import sys

class GameMain:
    def __init__(self):
        pygame.init self.screen = pygame.display.set_mode((SCREEN_WIDDTH, SCREEN_HEIGHT))
        self.states =
        {   "menu": MenuState(self),
            "play": PlayState(self),
            "pause": PauseState(self),
            "debug": DebugState(self),
        }
