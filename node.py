import pygame
from pygame.locals import *
import operator
from app import *

class Node:
    initial_pos = (0, 0)
    size = (10, 10)
    flow = (0, 1)
    gap = (0, 10)
    seq = 0
    def __init__(self, *args, **kwargs):
        for (k,v) in kwargs:
            match k:
                case 'size':
                    Node.size = v
                case 'flow':
                    Node.flow = v
                case 'gap':
                    Node.gap = v
                case 'pos':
                    Node.initial_pos = v
                    Node.seq = 0
                case _:
                    print('Node init: invalid arg')
        self.pos = (Node.initial_pos[0] + (Node.seq * Node.flow[0] * Node.gap[0]), Node.initial_pos[1] + (Node.seq * Node.flow[1] * Node.gap[1]))
        print(self.pos)
        Node.seq += 1
    def draw(self):
        pygame.draw.rect(App.screen, Color('RED'), (self.pos, tuple(map(operator.add, self.pos, Node.size))))
