import pygame
from token import Token

class Game_Square:
        def __init__(self, room, coord, occupant):
            self.room = room
            self.coord = coord
            self.occupant = occupant
            self.adjacencies = []
        def set_adjacent(*adjacent):
            for a in adjacent:
                adjacencies.append(a)
