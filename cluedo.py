# Example file showing a basic pygame "game loop"
import pygame
from pygame.locals import *
import random
from app import *
from scene import Scene
from node import *
#from board import Game_Board

class Cluedo(App):
    def __init__(self):
        super().__init__()
        Scene(img_folder='./assets', bgFile='Clue2012-board-ezgif.com-webp-to-jpg-converter.jpg', caption='Cluedo Board')
        App.scenes[0].nodes.append(Node())
        App.scenes[0].nodes.append(Node())
        App.scenes[0].nodes.append(Node())

if __name__ == '__main__':
    Cluedo().run()
"""global font
font = pygame.font.Font(None,40)
#global b
#b = Game_Board()

def write(text, location=(30,30), color=(0,0,0)):
    screen.blit(font.render(text,True,color),location)

global characters
characters = ["Green", "Mustard", "Peacock", "Plum", "Scarlet", "White"]
global weapons
weapons = ["Wrench", "Candlestick", "Dagger", "Pistol", "Lead Pipe", "Rope"]
global rooms
rooms = ["Bathroom", "Study", "Dining Room", "Games Room", "Garage", "Bedroom", "Living Room", "Kitchen", "Courtyard"]

global solution
global draw_pile

global game_state
game_stage = "Start"
class Player:
    def __init__(self):
        self.cards = []
        self.room = ""
        self.revealing = ""

global players
players = [Player(), Player(), Player(), Player()]

def suggest(character, weapon, room):
    print("Hi")


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((232,220,180))

    # RENDER YOUR GAME HERE
    if game_stage == "Start":
        c = characters.copy()
        w = weapons.copy()
        r = rooms.copy()
        c_m = random.choice(c)
        w_m = random.choice(w)
        r_m = random.choice(r)
        c.remove(c_m)
        w.remove(w_m)
        r.remove(r_m)
        draw_pile = c + w + r
        solution = [c_m, w_m, r_m]
        while len(draw_pile) >= len(players):
            for player in players:
                player.cards.append(random.choice(draw_pile))
                draw_pile.remove(player.cards[-1])
                player.room = random.choice(rooms)
    
    write(\"""Game contition:\n
        Player 1: Nothing Revealed, in Bedroom\n
        Player 2: Nothing Revealed, in Bathroom\n
        Player 3: Nothing Revealed, in Game Room\n
        Player 4: Nothing Revealed, in Living Room\n
        No Extra Cards\""")
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()"""
