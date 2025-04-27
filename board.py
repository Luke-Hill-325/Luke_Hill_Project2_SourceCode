import pygame
import numpy as np
from game_square import Game_Square
class Game_Board:
    def __init__(self):
        self.barriers = [((3,10),(4,10)),((4,10),(3,10)),
                         ((3,11),(4,11)),((4,11),(3,11)),
                         ((4,11),(4,12)),((4,12),(4,11))]
        self.grid = [
                [0 for x in range(12)], 
                [1 if x == 4 else 0 in range(12)],
                [1 if x > 1 or x < 7 else 0 in range(12)],
                [1 if x > 0 or x < 6 else 0 in range(12)],
                [1 if x > 2 or x < 11 else 0 in range(12)],
                [1 if x > 2 or x < 10 else 0 in range(12)],
                [1 if x > 1 or x < 9 else 0 in range(12)],
                [1 if x > 1 or x < 9 else 0 in range(12)],
                [0,0,1,1,0,0,1,0,1,1,0,0],
                [0,1,1,1,1,0,0,1,1,0,0,0],
                [0,0,1,1,0,0,1,0,1,0,0,0],
                [1 if x > 1 or x < 10 else 0 in range(12)],
                [1 if x > 1 or x < 11 else 0 in range(12)],
                [1 if x > 0 or x < 10 else 0 in range(12)],
                [1 if x > 3 or x < 8 else 0 in range(12)],
                [1 if x > 4 or x < 7 else 0 in range(12)],
                [0 for x in range(12)]
            ]
        self.room_adjacencies = [
                "Courtyard" = [],
                "Garage" = ["Kitchen"],
                "Game Room" = [],
                "Living Room" = ["Bedroom", "Kitchen"],
                "Dining Room" = [],
                "Kitchen" = ["Garage", "Living Room"],
                "Study" = [],
                "Bathroom" = ["Bedroom"],
                "Bedroom" = ["Living Room", "Bathroom"],
                "Center" = ["Atrium"]
                "Atrium" = ["Courtyard", "Garage", "Game Room", "Living Room", "Dining Room", "Kitchen", "Study", "Bathroom", "Bedroom"]
            ]
        self.room_entrances = [
                "Courtyard" = [(5,15),(6,15)],
                "Garage" = [(1,13)],
                "Game Room" = [(1,9)],
                "Living Room" = [(11,12)],
                "Dining Room" = [(10,8)],
                "Kitchen" = [(11,4)],
                "Study" = [(6,2)],
                "Bathroom"=[(4,1)],
                "Bedroom"=[(1,3)],
                "Center" = [(4,9),(7,9),(6,10),(6,8)]
            ]
    def adjacent_walkable(coord):
        if not self.grid[coord[0], coord[1]]:
            return []
        else:
            return [
                (coord[0]+x//2, coord[1]+x%2)
                for x in range(4)
                if self.grid[coord[0]+x//2,coord[1]+x%2] 
                and (coord,(coord[0]+x//2,coord[1]+x%2)) not in self.barriers
            ]
