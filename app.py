import pygame
from pygame.locals import *

class App:
    scenes = []
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((631, 640), flags)
        App.running = True
        self.clock = pygame.time.Clock()
        self.shortcuts = {
        }
        
    def do_shortcut(self, event):
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])
    def run(self):
        cur_scene = 0
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                elif event.type == KEYDOWN:
                    self.do_shortcut(event)
            App.scenes[cur_scene].draw()

